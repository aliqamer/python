
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

    def update_read_write_capacity(self, table_name, new_read_capacity, new_write_capacity):
        print("updating provisioned throughput of table with name " + table_name)
        return self._client.update_table(
            TableName=table_name,
            ProvisionedThroughput={
                'ReadCapacityUnits': new_read_capacity,
                'WriteCapacityUnits': new_write_capacity
            }
        )
