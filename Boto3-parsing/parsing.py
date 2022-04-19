import boto3
import json

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    bucket = 'bucket-for-aws-json'
    key = 'ip-ranges.json'

    obj = s3.Object(bucket, key)
    data = obj.get()['Body'].read().decode('utf-8')
    json_data = json.loads(data)
    
    for i in json_data["prefixes"]:
        print(i["ip_prefix"], i["region"])