import json

def lambda_handler(event, context):
    body = json.loads(event['body'])
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from api: {}'.format(body['api']))
    }