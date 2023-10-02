import boto3
from botocore.config import Config

ts_config = Config(
    region_name = 'us-east-2'
)

client = boto3.client('timestream-write', config=ts_config)