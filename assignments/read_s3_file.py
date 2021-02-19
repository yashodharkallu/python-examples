import requests
import boto3
from botocore import UNSIGNED
from botocore.client import Config

s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
for key in s3.list_objects(Bucket='coderbytechallengesandbox')['Contents']:
  if key['Key'].startswith('__cb__'):
    contents = s3.get_object(Bucket='coderbytechallengesandbox', Key=str(key['Key']))
    cont = contents['Body'].read().decode('utf-8')
    print(cont)
