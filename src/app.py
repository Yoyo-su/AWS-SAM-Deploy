import json

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

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    return respond(None, res="Hello, World!")