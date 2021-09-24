import boto3

client=boto3.client('dynamodb')

def handler(event, context):
  data = client.put_item(
    TableName='git-table',
    Item={
        'id': {
          'S': '005'
        },
        'price': {
          'N': '500'
        },
        'name': {
          'S': 'Yeezys'
        }
    }
  )
response = {
      'statusCode': 200,
      'body': 'successfully created data',
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response