import os
import json

import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.environ.get("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/voidful/wav2vec2-xlsr-multilingual-56"
headers = {"Authorization": "Bearer {HF_TOKEN}"}

def query_wav2vec(filename):
    print("entered wav2vec")
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()
