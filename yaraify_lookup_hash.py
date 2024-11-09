#!/usr/bin/python3
import requests
import urllib3
import json
import sys

if len(sys.argv) < 3:
    print("Looks up a file hash on YARAify")
    print("Usage: python3 yaraify_lookup_hash.py <YOUR-AUTH-KEY> <file-hash>")
    print("Note: If you don't have an Auth-Key yet, you can obtain one at https://auth.abuse.ch/")
    quit()

headers = {
    "Auth-Key"      :   sys.argv[1]
}

pool = urllib3.HTTPSConnectionPool('yaraify-api.abuse.ch', port=443, maxsize=50, headers=headers)

data = {
    'query':            'lookup_hash',
    'malpedia-token':   'xxx', # Your malpedia token. If you don't have any, simply obmit this field or keep it empty
    'search_term':      sys.argv[2]
}
json_data = json.dumps(data)
response = pool.request("POST", "/api/v1/", body=json_data)
response = response.data.decode("utf-8", "ignore")
print(response)
