import json

def handler(event, context):
    print(event)
    print('request: {}'.format(json.dumps(event)))

    accepted_json = event['queryStringParameters']

    parameters = [
        'username',
        'yearly_earnings',
        'birth_date',
        'email'
    ]

    missing_params = parameters
    if accepted_json != {}:
        missing_params = [x for x in parameters if x not in accepted_json]

    if missing_params != []:
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'text/plain'
            },
            'body': 'Missing Parameters: %s' % missing_params
        }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Thanks for the bank information bruh'
    }