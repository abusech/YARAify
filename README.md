# YARAify
YARAify is an open YARA scan- and search engine. This repository provides some sample python3 scripts on how to interact with the YARAify API.

## Obtain an Auth-Key
In order to query the YARA API, you need to obtain an ```Auth-Key```.  If you don't have an Auth-Key yet, you can get one at https://auth.abuse.ch/ for free.

## Submit a file for YARA scanning
This script calls the [scan endpoint](https://yaraify.abuse.ch/api/#file-scan) to scan a file using the YARAify service.

```
python3 yaraify_submit.py <path-to-file>
```

Pro tip: Before you start using our YARA scan engine, we recommend you to have a look at the various paramenters you can use to customize your submission:

https://yaraify.abuse.ch/api/#file-scan

## Lookup file hash (MD5, sha256, SHA1 or SHA3-384 hash)
This scripts calls the [hash lookup endpoint](https://yaraify.abuse.ch/api/#query-filehash) to lookup up a hash (MD5, SHA256, SHA1 or SHA3-384 hash) in the YARAify database:

```
python3 yaraify_lookup_hash.py 97e8b8205a9be4ddbed90d7c354a58aab170c15e458564baee9f50e17ca79649
```

## Lookup YARA rule matches
This script calls the [YARA lookup endpoint](https://yaraify.abuse.ch/api/#yara) to get recent files matching a specific YARA rule.

```
python3 yaraify_lookup_yara-rule.py CobaltStrikeBeacon 50
```

## Lookup a task ID
This script calls the [task ID endpoint](https://yaraify.abuse.ch/api/#query-taskid), looking up a particular task ID in the YARAify databasel:

```
python3 yaraify_check_taskid.py cfa49f83-6d98-11ed-a71a-42010aa4000b
```

## List tasks for an identifier
YARAify provides you an easy way to track your YARA scans without the need of e.g. signing up for an account: identifiers! Before you start using identifiers to keep track of your submissions, we recommend you to have a look at the corresponding documentation:

https://yaraify.abuse.ch/api/#identifiers

Once you created your own (private) identifier and submited files to the YARAify YARA scan engine, you can use this script to get a list of recent tasks. If you e.g. want to get a list of queued tasks associated with your identifier, you can use the script as follow:

```
python3 yaraify_list_tasks.py <identifier> queued
```

## Deploy a YARA rule for live hunting
This script calls the endpoint for [deploying a YARA rule](https://yaraify.abuse.ch/api/#deploy-yara) to conduct live hunting on YARAify with your own rule.

```
python3 upload_yara_rule.py <YOUR-AUTH-KEY> <yara-rule-file>
```

## API documentation

The documentation for the YARAify API is available here:

https://yaraify.abuse.ch/api/
