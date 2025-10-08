import json

def handler(event, context):
    """
    A simple Lambda function that returns a greeting.
    """
    print("Lambda function invoked!")
    print(f"Event received: {json.dumps(event)}")

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": "ppSync consumer Lambda function executed successfully!",
            "input": event
        })
    }
