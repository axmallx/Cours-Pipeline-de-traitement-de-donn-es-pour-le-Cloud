import datetime
import json
import random
import boto3

STREAM_NAME = "input-stream"
REGION = "eu-north-1"

def get_data():
    return {
        'event_time': datetime.datetime.now().isoformat(),
        'ticker': random.choice(["AMMI","ETH","BNB", "XRP", "DOGE","SEBO"]),
        'price': round(random.random() * 100, 2)}

def generate(stream_name, kinesis_client):
    while True:
        data = get_data()
        print(data)
        kinesis_client.put_record(StreamName=stream_name,Data=json.dumps(data),PartitionKey="partitionkey")

if _name_ == '_main_':
    generate('amal-mimouni-stock-input-stream', boto3.client('kinesis', 
aws_access_key_id="AKIA4P4ZQJMIPWJJ5VFD",
aws_secret_access_key="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", 
region_name="eu-north-1"))