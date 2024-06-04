import json

def handler(event, context):
    print(event)
    print('request: {}'.format(json.dumps(event)))

    parameters = [
        'username',
        'yearly_earnings',
        'birth_date',
        'email'
    ]
    missing_params = [x for x in event.keys() if x in parameters]
    if len(missing_params) != 4:
        needed_params = [x for x in parameters if x not in missing_params]
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'text/plain'
            },
            'body': 'Missing Parameters: %s' % needed_params
        }



    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Thanks for the bank information bruh'
    }