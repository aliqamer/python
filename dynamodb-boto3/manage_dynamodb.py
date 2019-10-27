from src.client_factory import DynamoDBClient
from src.dynamodb import DynamoDB


def create_dynamodb_table():
    dynamodb_client = DynamoDBClient().get_client()
    dynamodb = DynamoDB(dynamodb_client)

    table_name = "Movies"

    # define attributes
    attribute_definitions = [
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        }
    ]

    # define key_schema
    key_schema = [
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  # partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  # sort key
        }
    ]

    initial_iops = {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }

    dynamodb_create_table_response = dynamodb.create_table(
        table_name, attribute_definitions, key_schema, initial_iops)
    print('Created DynamoDB Table name ' + table_name +
          ' : ' + str(dynamodb_create_table_response))


if __name__ == '__main__':
    import sys
    create_dynamodb_table()
