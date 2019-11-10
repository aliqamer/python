import json
import boto3


def start_stop_ec2_instances_with_autoscaling(event, context):

    autoscaling_client = boto3.client('autoscaling')

    count = 1
    if count > 0:
        count = 1
    else:
        count = 0
    response = auto_scale(autoscaling_client, count)
    print('autoscaling response: '+response)

    message = 'Environment is started, wait for 15 min for bootup time'

    if count == 0:
        message = 'Thank you for shutting down environment!'

    body = {
        "message": message
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
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

    return autoscaling_client.set_desired_capacity(
        AutoScalingGroupName='my-auto-scaling-group',
        DesiredCapacity=count,
        HonorCooldown=True,
    )
