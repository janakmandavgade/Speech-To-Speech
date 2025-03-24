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
	# print("Resoponse content", response.content)
	# print("Resoponse json", response.json())
	return response.content


# audio_bytes = query_fbookmmsttsen({
# 	"inputs": "The answer to the universe is 42",
# })

# directory = "results"
# filename = f"results_{timestamp}.wav"

# os.makedirs(directory, exist_ok=True)


# audio_data, samplerate = sf.read(io.BytesIO(audio_bytes), format='RAW', channels=1, samplerate=16000, subtype='PCM_16')
# sf.write('output.wav', audio_data, samplerate)
# with open('output.wav', 'wb') as f:
#     f.write(audio_bytes)

# with open(f"{directory}/{filename}", 'wb') as f:
#     f.write(audio_bytes)