from src.client_locator import EC2Client
from src.ec2.ec2 import EC2
from src.ec2.vpc import VPC


def main():
    # creating vpc
    ec2_client = EC2Client().get_client()
    vpc = VPC(ec2_client)

    vpc_response = vpc.create_vpc()

    print('VPC created: '+str(vpc_response))

    # add name tag to VPC
    vpc_name = 'Boto3_VPC'
    vpc_id = vpc_response['Vpc']['VpcId']
    vpc.add_name_tag(vpc_id, vpc_name)

    print('Added ' + vpc_name + ' to '+vpc_id)

    # Create an IGW
    igw_response = vpc.create_internet_gateway()

    igw_id = igw_response['InternetGateway']['InternetGatewayId']

    vpc.attach_igw_to_vpc(vpc_id, igw_id)

    # Create a public subnet
    public_subnet_respone = vpc.create_subnet(vpc_id, '10.0.1.0/24')

    public_subnet_id = public_subnet_respone['Subnet']['SubnetId']

    print('Subnet created for VPC '+vpc_id+':' + str(public_subnet_respone))

    # Add name tag to Public Subnet
    vpc.add_name_tag(public_subnet_id, 'Boto3-Public-Subnet')

    # Create a public route table
    public_route_table_response = vpc.create_public_route_table(vpc_id)

    rtb_id = public_route_table_response['RouteTable']['RouteTableId']

    # Adding IGW to public route table
    vpc.create_igw_route_to_public_route_table(rtb_id, igw_id)

    # Associate public subnet with Route Table
    vpc.associate_subnet_with_route_table(public_subnet_id, rtb_id)

    # Allow auto-assign public ip addresses for subnet
    vpc.allow_auto_assign_ip_addresses_for_subnet(public_subnet_id)

    # Create a Private Subnet
    private_subnet_response = vpc.create_subnet(vpc_id, '10.0.2.0/24')
    private_subnet_id = private_subnet_response['Subnet']['SubnetId']

    print('Created private subnet '+private_subnet_id+' for VPC '+vpc_id)

    # Add name tag to Private Subnet
    vpc.add_name_tag(private_subnet_id, 'Boto3-Private-Subnet')

    # EC2 Instances
    ec2 = EC2(ec2_client)

    # Create a kay pair
    key_pair_name = 'Boto3-KeyPair'
    key_pair_response = ec2.create_key_pair(key_pair_name)

    print('Created Key Pair with name ' +
          key_pair_name+':'+str(key_pair_response))

    # Create a Security Group
    public_security_group_name = 'Boto3-Public-SG'
    public_security_group_description = 'Public SG for public subnet internet access'
    public_sg_response = ec2.create_security_group(
        public_security_group_name, public_security_group_description, vpc_id)

    public_sg_id = public_sg_response['GroupId']

    # Add Public Access to Security Group
    ec2.add_inbound_rule_to_sg(public_sg_id)

    print('Added public access rule to Security Group '+public_security_group_name)

    user_data = """#!/bin/bash
                   yum update -y
                   yum install httpd24 -y
                   service httpd start
                   chkconfig httpd on
                   echo "<html><body><h1>Hello from <b>Boto3</b> using Python!</h1></body></html>" > /var/www/html/index.html """

    ami_id = 'ami-1b316af0'

    # Launch a public EC2 Instance
    ec2.launch_ec2_instance(ami_id, key_pair_name,
                            1, 1, public_sg_id, public_subnet_id, user_data)

    print('Launching Public EC2 instance using AMI ami-1b316af0')

    # Adding another Security Group for Private EC2 Instance

    private_security_group_name = 'Boto3-Private-SG'
    private_security_group_description = 'Private SG for private subnet'
    private_sg_response = ec2.create_security_group(
        private_security_group_name, private_security_group_description, vpc_id)

    private_sg_id = private_sg_response['GroupId']

    # Add rule to private secruity group
    ec2.add_inbound_rule_to_sg(private_sg_id)

    # Launch a private EC2 Instance
    ec2.launch_ec2_instance(ami_id, key_pair_name,
                            1, 1, private_sg_id, private_subnet_id, """""")


if __name__ == '__main__':
    main()
