
class EC2:
    def __init__(self, client):
        self._client = client
        """ :type : pyboto3.ec2 """

    def create_key_pair(self, key_name):
        print('Creating a key pair with name '+key_name)
        return self._client.create_key_pair(KeyName=key_name)

    def create_security_group(self, group_name, description, vpc_id):
        print('Creating a Security Group with name ' +
              group_name+' for VPC '+vpc_id)
        return self._client.create_security_group(
            GroupName=group_name,
            Description=description,
            VpcId=vpc_id
        )
