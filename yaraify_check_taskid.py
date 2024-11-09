#!/usr/bin/python3
import requests
import urllib3
import json
import sys

if len(sys.argv) < 3:
    print("Query YARAify for a task ID")
    print("Usage: python3 yaraifier_check_taskid.py <YOUR-AUTH-KEY> <task_id>")
    print("Note: If you don't have an Auth-Key yet, you can obtain one at https://auth.abuse.ch/")
    quit()

headers = {
    "Auth-Key"      :   sys.argv[1]
}

pool = urllib3.HTTPSConnectionPool('yaraify-api.abuse.ch', port=443, maxsize=50, headers=headers)

data = {
    'query':            'get_results',
    'malpedia-token':   'xxx', # Your malpedia token. If you don't have any, simply obmit this field or keep it empty
    'task_id':          sys.argv[2]
}
json_data = json.dumps(data)
response = pool.request("POST", "/api/v1/", body=json_data)
response = response.data.decode("utf-8", "ignore")
print(response)
