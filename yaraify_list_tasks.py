#!/usr/bin/python3
import requests
import urllib3
import json

pool = urllib3.HTTPSConnectionPool('yaraify.abuse.ch', port=443, maxsize=50, cert_reqs='CERT_NONE', assert_hostname=True)

data = {
    'query':            'list_tasks',
    'identifier':        'YOUR-IDENTIFIER', # Your identifier
    'task_status':	 'queued'
}
json_data = json.dumps(data)
response = pool.request("POST", "/api/v1/", body=json_data)
response = response.data.decode("utf-8", "ignore")
print(response)
