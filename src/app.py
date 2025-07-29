import json
import boto3
import os

print("Loading function")

# create a DynamoDB client
region_name = 'eu-west-2'
dynamodb = boto3.client('dynamodb', region_name=region_name)
table_name = os.environ['TABLE_NAME']

# Function to respond with a standardized API format
def respond(err, res=None):
    if err:
        return {
            "statusCode": 400,
            "body": f"Error: {err.message}"
        }
    else:
        return {
            "statusCode": 400 if err else 200,
            "body": err.message if err else  json.dumps(res),
            "headers": {
                "Content-Type": "application/json"
            }            
        }

# Lambda handler function
def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    try:
        scan_result = dynamodb.scan(TableName=table_name)
        return respond(None, res=scan_result)
    except Exception as e:
        print(f"Error scanning DynamoDB table: {e}")
        return respond(e)
