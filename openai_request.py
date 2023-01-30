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
    "prompt": "Das höchste Gebäude in Deutschland",
    "temperature": 0,
    "max_tokens": 500
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    json_response = json.loads(response.content)
    print(json_response["choices"][0]["text"])
else:
    print("Error: ", response.content)