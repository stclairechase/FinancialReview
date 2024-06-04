import json

def handler(event, context):
    print(event)
    print('request: {}'.format(json.dumps(event)))

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Thanks for the bank information bruh'
    }