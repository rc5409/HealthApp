# patientchat/views.py
import requests

from django.shortcuts import render
import requests

def home_view(request):
    return render(request, 'patientchat/home.html')

def together_ai_view(request):
    url = "https://api.together.xyz/inference"
    payload = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "prompt": "<s>[INST] What is the capital of France? [/INST]",
        "max_tokens": 512,
        "stop": ["</s>", "[/INST]"],
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "repetition_penalty": 1,
        "n": 1
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer 5993e5c469e98d13cd5d7bd5ba68fa2fc01921237deb19ef1a25ac53e2ea9c34"
    }

    response = requests.post(url, json=payload, headers=headers)
    response_data = response.json()

    return render(request, 'patientchat/together_ai_response.html', {'response_data': response_data})

