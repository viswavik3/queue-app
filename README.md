# Azure Queue Fixed Lab

## Key Fixes
- No queue initialization at startup
- Safe env variable handling
- Prevents App Service crash

## IMPORTANT
Set ONE of these in App Service:

AZURE_STORAGE_CONNECTION_STRING

## Run

python app.py
python worker.py

## Deploy

az webapp deployment source config-zip --src azure_queue_fixed_lab.zip
