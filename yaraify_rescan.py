#!/usr/bin/env python
import logging
import requests
import urllib3
import json
import time
import sys


if len(sys.argv) < 2:
    print("Trigger a re-scan of a file")
    print("Usage: python3 yaraify_rescan.py <file-hash>")
    print("Note: hash can be a MD5, SHA1, SHA256 or SHA3-384 hash")
    quit()

logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)-8s %(message)s')
headers = {
    "Auth-Key"      :   "YOUR-AUTH-KEY-HERE" # You can get one here: https://auth.abuse.ch/user/me
}
pool = urllib3.HTTPSConnectionPool('yaraify-api.abuse.ch', port=443, maxsize=50, headers=headers)


def rescan_yaraify(hash):
    data = {
        'query':    'rescan_file',
        'hash':     hash
    }
    json_data = json.dumps(data)
    response = pool.request("POST", "/api/v1/", body=json_data)
    response = response.data.decode("utf-8", "ignore")
    data = json.loads(response)
    logging.info(f"{hash} queued for re-scan with task ID {data['data']['task_id']}")
    return data['data']['task_id']

def check_taskid(task_id):
    data = {
        'query':    'get_results',
        'malpedia-token':   'xxx', # Your malpedia token. If you don't have any, simply obmit this field or keep it empty
        'task_id':  task_id
    }
    json_data = json.dumps(data)
    response = pool.request("POST", "/api/v1/", body=json_data)
    response = response.data.decode("utf-8", "ignore")
    return json.loads(response)



task_id = rescan_yaraify(sys.argv[1]) # hash 
while True:
    data = check_taskid(task_id)
    if data['data'] == 'queued':
        logging.info(f"{task_id} is queued")
        time.sleep(1)
        continue
    logging.info(f"{task_id} is done")
    print(json.dumps(data['data'], indent=2))
    break
