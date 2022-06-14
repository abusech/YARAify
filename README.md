# YARAify
YARAify

You can find a few python3 code examples in this repository on how to interact with the YARAify API:

- yaraify_check_taskid.py: Lookup a task ID
- yaraify_list_tasks.py: List most recent tasks associated with an ```identifier```
- yaraify_submit.py: Submit a file to YARAify for scanning

Note: When interacting with the YARAify API, we recommend you to use ```urllib3.HTTPSConnectionPool``` whenver possible. This will re-use existing HTTPs connections instead of creaing a new one for every request
