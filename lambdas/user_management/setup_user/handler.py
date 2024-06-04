
import re

def handler(event, context):
    print(event)

    sent_params = event['queryStringParameters']
    valid_data = True

    possible_params = [
        'username',
        'email',
        'birthdate'
    ]

    missing_params = possible_params
    if sent_params != {}:
        missing_params = [x for x in possible_params if x not in sent_params]
        error_message = 'Missing Parameters: %s' % missing_params
        valid_data = False
    

    if valid_data != True: 
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'text/plain'
            },
            'body': error_message
        }
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Thanks for the bank information bruh'
    }