import json
import boto3

def lambda_handler(event, context):
    s3_resource = boto3.resource('s3')
    mybucket = s3_resource.Bucket('s3-bucket-for-lambda-2')
    key = 'notification-members.csv'

    sns_client = boto3.client('sns')
    
    objs = list(mybucket.objects.filter(Prefix=key))
    
    if objs:
        print('the file sends notification')
        sns_client.publish(TopicArn='arn:aws:sns:us-east-1:323867645900:Lambdha-practice-with-s3',Message='added to s3',Subject='s3 data')
    else:
        print("the file not present")