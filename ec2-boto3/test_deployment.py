from src.client_locator import EC2Client
from src.ec2.vpc import VPC


def main():
    # creating vpc
    ec2_client = EC2Client().get_client()
    vpc = VPC(ec2_client)

    vpc_response = vpc.create_vpc()

    print('VPC created: '+str(vpc_response))


if __name__ == '__main__':
    main()
