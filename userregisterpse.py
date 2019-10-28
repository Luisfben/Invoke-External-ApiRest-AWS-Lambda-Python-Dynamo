import json
import urllib2

def handler(event, context):

    id = event.get('pathParameters').get('id')

    apiurl = 'https://4lznc7dtc7.execute-api.us-east-1.amazonaws.com/dev/payonline/externalservice/' + id
   
    response = urllib2.urlopen(apiurl)
   
    html = response.read()
   
    if html == 'null':
        registrado = 'N'
    else:
        registrado ='S'
       
    result = {
      'id': id,
      'registrado': registrado
    }
   
    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response