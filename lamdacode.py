import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    s3_bucket = "task4buckett"
    file_name = "details.txt"

    response = s3.get_object(Bucket=s3_bucket, Key=file_name)
    aary = response['Body'].read().decode('utf-8').splitlines()

    return aary
