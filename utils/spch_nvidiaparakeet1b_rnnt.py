import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.environ.get("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/nvidia/parakeet-rnnt-1.1b"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query_nvidiaparakeet(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

# output = query_nvidiaparakeet("whatisnode.js.mp3")
# print(output)