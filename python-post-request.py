import requests
import json

api_url = 'https://api_endpoint_url'
file_abs_url = '/file/absolute/path'
auth_token = 'bearer_token'

payload = {
    'property1':'value1',
    'property2':'value2',
    'property3':'value3',
    'array_1':[
        {'property1':'value1', 'property2':'value2', 'property3':'value3'},
        {'property1':'value1', 'property2':'value2', 'property3':'value3'},
    ],
}

files = {
    'json_data': (None, json.dumps(payload), 'application/json'),
    'file': ('file_abs_url', open('file_abs_url', 'rb'), 'application/octet-stream')
}

headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'Authorization': 'Bearer ' + auth_token,
}

r = requests.post( api_url, files=files, headers=headers )

print(r.text)
