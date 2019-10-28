
class DynamoDB:
    def __init__(self, client):
        self._client = client
        """ :type : pyboto3.dynamodb """

    def create_table(self, table, attribute_definitions, key_schema, iops):
        print('creating dynamodb table...')
        return self._client.create_table(
            TableName=table,
            AttributeDefinitions=attribute_definitions,
            KeySchema=key_schema,
            ProvisionedThroughput=iops
        )

    def describe_table(self, table):
        print("Describing Dynamodb table name: "+table)
        return self._client.describe_table(TableName=table)