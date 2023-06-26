import requests
import json

def get_response(message):
    url = "https://api.cohere.ai/v1/infer"
    headers = {
        "Authorization": "l0nxA2GdkkkQYgsjZJ6HRTtDfaRBE4vlpHXGWxNx",
        "Content-Type": "application/json",
    }
    data = {
        "model": "edith-8527",
        "prompt": message,
        "max_tokens": 600,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()["output"]
    else:
        return "Sorry, I couldn't process that request."
