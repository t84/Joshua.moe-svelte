import requests
import json

# Replace this with your actual deployed Cloudflare Worker URL
ENDPOINT = "https://floral-cherry-625c.latebat.workers.dev"

payload = {
    "name": "Bob",
    "message": "Trying the embed version!"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(ENDPOINT, headers=headers, data=json.dumps(payload))

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
