import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.environ.get("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/intfloat/e5-mistral-7b-instruct"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def querytomistral(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
# output = query({
# 	"inputs": "Today is a sunny day and I will get some ice cream.",
# })