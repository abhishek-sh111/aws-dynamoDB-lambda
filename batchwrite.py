import json

import boto3 

client = boto3.resource('dynamodb')
table = client.Table('git-table')
def lambda_handler(event, context):
    with table.batch_writer() as batch:
        batch.put_item(
            Item={
              'id':'1243',
               
                'first_name': 'abhishek',
                'last_name': 'srungeri',
                'age': 24,
                'address': {
                    'road': 'near society bank',
                    'city': 'Los Angeles',
                    'state': 'CA',
                    'zipcode': 520139
                }
            }
        )
        batch.put_item(
            Item={
              'id':'13453',
               
            'first_name': 'kane',
            'last_name': 'williamson',
            'age': 40,
            'address': {
                'road': '2 Washington Avenue',
                'city': 'Cali',
                'state': 'WA',
                'zipcode': 232432
            }
        }
        )
     
       
    response = {
      'statusCode': 200,
      'body': 'Successfully Updated',
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
    }
  
    return response
