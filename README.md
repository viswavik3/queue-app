# Azure Queue WebJob Lab

## What this includes
- Flask Web App (UI)
- Azure Storage Queue integration
- Continuous WebJob worker


## Setup

1. Create queue:
az storage queue create --name demo-queue --account-name <your-storage>

2. Set env var in App Service:
AZURE_STORAGE_CONNECTION_STRING

## Deploy

az webapp deployment source config-zip --src azure_queue_webjob_lab.zip

## Verify

Go to App Service → WebJobs
Check "queue-worker" is running

## Test

- Add message in UI
- Check WebJob logs
