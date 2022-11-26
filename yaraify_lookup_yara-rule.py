#!/usr/bin/python3
import requests
import urllib3
import json
import sys

if len(sys.argv) < 3:
    print("Usage: python3 yaraify_lookup_yara-rule.py <yara-rule-name> <limit>")
    quit()

pool = urllib3.HTTPSConnectionPool('yaraify-api.abuse.ch', port=443, maxsize=50)

data = {
    'query':            'get_yara',
    'search_term':      sys.argv[1],
    'result_max':       sys.argv[2]
}
json_data = json.dumps(data)
response = pool.request("POST", "/api/v1/", body=json_data)
response = response.data.decode("utf-8", "ignore")
print(response)
