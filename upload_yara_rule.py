#!/usr/bin/env python3
import requests
import sys
import json

if len(sys.argv) < 3:
    print("Upload a YARA rule to YARAify for live hunting")
    print("Usage: python3 upload_yara_rule.py <YOUR-AUTH-KEY> <yara-rule-file>")
    print("Note: If you don't have an Auth-Key yet, you can obtain one at https://auth.abuse.ch/")
    quit()

headers = {
    "Auth-Key"      :   sys.argv[1]
}

files = {
    'yara_file': (open(sys.argv[2],'rb'))
}

response = requests.post('https://yaraify-api.abuse.ch/api/v1/', files=files, verify=True, headers=headers)
print(response.content.decode("utf-8", "ignore"))
