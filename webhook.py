import requests
import json

webhook_url = 'https://webhooklistener.cp.eks.qa.useast1.cloudtrust.rocks/webhook'

data = { 'name': 'AlertAutomationTest',
         'URL': 'Test URL'}

r=requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})