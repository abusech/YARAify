#!/usr/bin/python3
import requests
import urllib3
import json
import sys

if len(sys.argv) < 4:
    print("Lists YARAify tasks associated with a specific identifier")
    print("Usage: python3 yaraify_list_tasks.py <identifier> <task-status>")
    print("Note: If you don't have an Auth-Key yet, you can obtain one at https://auth.abuse.ch/")
    quit()

headers = {
    "Auth-Key"      :   sys.argv[1]
}

pool = urllib3.HTTPSConnectionPool('yaraify-api.abuse.ch', port=443, maxsize=50, headers=headers)

data = {
    'query':            'list_tasks',
    'identifier':       sys.argv[2],
    'task_status':	    sys.argv[3]
}
json_data = json.dumps(data)
response = pool.request("POST", "/api/v1/", body=json_data)
response = response.data.decode("utf-8", "ignore")
print(response)
