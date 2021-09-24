
import json

import boto3 

client = boto3.resource('dynamodb')
table = client.Table('git-table')
def lambda_handler(event,context):
   table.update_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': 29
    }
    )
response = {
      'statusCode': 200,
      'body': 'successfully updated',
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response