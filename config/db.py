import boto3

session = boto3.Session(
    aws_access_key_id='',
    aws_secret_access_key='',
    region_name='us-east-2'  
)

dynamodb = session.resource('dynamodb')
