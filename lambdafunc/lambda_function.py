import boto3
import json

dynamodb = boto3.client('dynamodb')
def handler(event, context):
    response = dynamodb.update_item(
        TableName='Res2Counter',
        Key={
            'Site': {
                'N': '0'
            }
        },
        UpdateExpression='SET Visits = Visits + :inc',
        ExpressionAttributeValues={
            ':inc': {'N': '1'}
        },
        ReturnValues="UPDATED_NEW"
    )
    res = dynamodb.get_item(
        TableName='Res2Counter',
        Key={
            'Site': {
                'N': '0'
            }
        },
        ProjectionExpression='Visits',
    )
    count = response['Attributes']['Visits']['N']
    print(res)
    vCount = int(count)
    return {
        'statusCode': 200,
        'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        },
        'body': json.dumps(vCount)
        }