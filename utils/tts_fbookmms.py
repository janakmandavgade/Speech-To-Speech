import requests
import scipy
import io
import soundfile as sf
import time
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.environ.get("HF_TOKEN")

API_URL = "https://router.huggingface.co/hf-inference/models/facebook/mms-tts-eng"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query_fbookmmsttsen(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	# print("Response content", response.content)
	# print("Resoponse json", response.json())
	return response.content