import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.environ.get("HF_TOKEN")

print("HF_TOKEN: ", HF_TOKEN)
API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query_whisperlargev3(filename):
    print("insidewhisper")
    with open(filename, "rb") as f:
        data = f.read()
    print("2 whisper")
    response = requests.post(API_URL, headers=headers, data=data)
    print("3 whisper")
    print(response)
    return response.json()

# output = query("sample1.flac")