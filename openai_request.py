import openai
import json
import requests


def test_quest():
    print(request_gpt("Höchste Gebäude Europas"))


def request_gpt(question:str):

    try:
        with open("C:/gptkey/gptkey.txt","r") as file:
            mykey = file.read()
    except:
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
        "prompt": question,
        "temperature": 0.6,
        "max_tokens": 200
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        json_response = json.loads(response.content)
        return json_response["choices"][0]["text"]
    else:
        return "Error: ", response.content



if __name__ == "__main__":
    test_quest()