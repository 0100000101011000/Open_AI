# import os
import openai
import json
import requests

mykey = "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"

openai.organization = "org-I9o2AkEBNABq4qZXcuBuhS8L"
openai.api_key = mykey
openai.Model.list()

url = "https://api.openai.com/v1/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {mykey}"
}

data = {
    "model": "text-davinci-003",
    "prompt": "Say this is a test",
    "temperature": 0,
    "max_tokens": 7
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    json_response = json.loads(response.content)
    print(json_response["choices"][0]["text"])
else:
    print("Error: ", response.content)