import json
import boto3

def lambda_handler(event, context):

    autoscaling_client = boto3.client('autoscaling')
    
    # accept request param as start=1 or 0
    startValue = event["queryStringParameters"]['start']

    if startValue.isnumeric() == False:
        return {
            "statusCode": 400,
            "body": "Invalid request!"
        }
    
    count = int(startValue)    
    
    if count > 0:
        count = 1
    else:
        count = 0
    response = auto_scale(autoscaling_client, count)
    print('autoscaling response: '+str(response))

    message = 'Environment is started, wait for 15 min for bootup time'

    if count == 0:
        message = 'Thank you for shutting down environment!'

    body = {
        "message": message
    }

    response = {
        "statusCode": 200,
        "body": message
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """


def auto_scale(autoscaling_client, count):

    return autoscaling_client.update_auto_scaling_group(
        AutoScalingGroupName='NotifyCoreGatewayECSClusterdev-EcsAutoScalingGroup-8E1KR7QP4WSQ',
        DesiredCapacity=count,
        MinSize=count
    )
