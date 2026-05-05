# Azure Storage Queue Full Lab

## What this lab covers

- Enqueue / Dequeue
- Visibility timeout
- Retry behavior
- Duplicate processing
- Queue buffering
- Slow processing impact

## Setup

Set environment variable:

AZURE_STORAGE_CONNECTION_STRING

## Run locally

Web UI:
python app.py

Worker:
python worker.py

## Test Scenarios

1. Normal:
   hello

2. Failure:
   fail-test

3. Slow processing:
   slow-task

4. Bulk load:
   Add 50 messages

5. Duplicate:
   Run 2 workers

## Deploy

zip and deploy:

az webapp deployment source config-zip --src app.zip
