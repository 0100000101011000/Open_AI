import openai
import json
import requests
step = 0

def testRequest(key:str):
    try:
        request_gpt("Hallo", key)
        return "Valid key"
    except:
        return "Invalid key"


def request_gpt(question:str, key:str):

    openai.organization = "org-I9o2AkEBNABq4qZXcuBuhS8L"
    openai.api_key = key
    openai.Model.list()
   
    url = "https://api.openai.com/v1/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }

    data = {
        "model": "text-davinci-003",
        "prompt": question,
        "temperature": 0.6,
        "max_tokens": 200
    }
    print("Jawoll1")
    response = requests.post(url, headers=headers, json=data)
    print(response.status_code)
    if response.status_code == 200:
        
        json_response = json.loads(response.content)
        answere = json_response["choices"][0]["text"]
        print("Jawoll3")
        return answere
    else:
        return "Error: ", response.content
