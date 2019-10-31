from src.client_locator import EC2Client
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


if __name__ == '__main__':
    main()
