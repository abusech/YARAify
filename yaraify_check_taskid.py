#!/usr/bin/python3
import requests
import urllib3
import json
import sys

if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    print("Usage: python3 yaraifier_check_taskid.py <task_id>")
    quit()

pool = urllib3.HTTPSConnectionPool('yaraify-api.abuse.ch', port=443, maxsize=50, cert_reqs='CERT_NONE', assert_hostname=True)

data = {
    'query':            'get_results',
    'malpedia-token':   'xxx', # Your malpedia token. If you don't have any, simply obmit this field or keep it empty
    'task_id':          sys.argv[1]
}
json_data = json.dumps(data)
response = pool.request("POST", "/api/v1/", body=json_data)
response = response.data.decode("utf-8", "ignore")
print(response)
