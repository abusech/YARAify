#!/usr/bin/env python3
import requests
import sys
import json

if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    print("Usage: python3 yaraifier_submit.py <file>")
    quit()

data = {
    'clamav_scan':   1,
    'unpack': 0,
    'skip_known': 0,
}
files = {
    'json_data': (None, json.dumps(data), 'application/json'),
    'file': (open(file,'rb'))
    }
response = requests.post('https://yaraify-api.abuse.ch/api/v1/', files=files, verify=True)
print(response.content.decode("utf-8", "ignore"))
