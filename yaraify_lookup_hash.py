#!/usr/bin/python3
import requests
import urllib3
import json
import sys

if len(sys.argv) < 2:
    print("Usage: python3 yaraify_lookup_hash.py <file-hash>")
    quit()

pool = urllib3.HTTPSConnectionPool('yaraify-api.abuse.ch', port=443, maxsize=50)

data = {
    'query':            'lookup_hash',
    'malpedia-token':   'xxx', # Your malpedia token. If you don't have any, simply obmit this field or keep it empty
    'search_term':      sys.argv[1]
}
json_data = json.dumps(data)
response = pool.request("POST", "/api/v1/", body=json_data)
response = response.data.decode("utf-8", "ignore")
print(response)
