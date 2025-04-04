import os
import time
import soundfile as sf
import gradio as gr
import scipy

from utils.spch_whisperlargev3 import query_whisperlargev3
from utils.gemini import querygemini
from utils.tts_fbookmms import query_fbookmmsttsen
from fastapi import FastAPI

app = FastAPI()

@app.get('/health')
async def root():
    """Health check for app"""
    return "App is running at /",200

def getAnswer(filepath):
    """
    Takes in a audio file path and generates LLM Responses.
    """
    if not os.path.exists(filepath):
        raise Exception("Audio file not found!")
    
    print(f"Processing file: {filepath}")
    que = query_whisperlargev3(filepath)
    
    if 'text' not in que:
        raise Exception("Failed to process audio.")
    
    output = querygemini(que['text'])
    print(f"AI Response: {output}")
    return output

def save_audio_file(audio):
    """
    Save audio file in directory and return path.
    """

    if audio is None:
        raise Exception("No audio input detected.")
    
    rate, y = audio
    timestamp = int(time.time())
    audio_folder = "audio"
    os.makedirs(audio_folder, exist_ok=True)
    
    # Save in multiple formats
    flac_filename = os.path.join(audio_folder, f"recording_{timestamp}.flac")
    mp3_filename = os.path.join(audio_folder, f"recording_{timestamp}.mp3")
    
    try:
        # Save as FLAC
        sf.write(flac_filename, y, rate, format='FLAC')
        
        # Save as MP3 (requires soundfile and pydub)
        # import pydub
        # sf.write(mp3_filename.replace('.mp3', '.wav'), y, rate)
        # sound = pydub.AudioSegment.from_wav(mp3_filename.replace('.mp3', '.wav'))
        # sound.export(mp3_filename, format='mp3')
        # os.remove(mp3_filename.replace('.mp3', '.wav'))
        
        return flac_filename
    except Exception as e:
        raise Exception(f"Error saving audio: {str(e)}")

def generate_audio_output(flac_filepath):
    """
    Convert the answer to audio data in bytes and return to gradio for display.
    """

    ans = getAnswer(flac_filepath)
    audio_bytes = query_fbookmmsttsen({"inputs": ans})
    if not audio_bytes:
        raise Exception("Received empty audio from AI model.")
    try:
        return audio_bytes,ans
    except Exception as e:
        raise Exception(f"Error processing audio output: {str(e)}")

def process_audio(audio):
    """Used to complete the pipeline of saving input audio file, coverting to text, 
    then getting LLM response and converting that to audio."""

    try:
        flac_filepath = save_audio_file(audio)
        audio_bytes, ai_gen_text = generate_audio_output(flac_filepath)
        print("Generated audio output successfully.")
        return audio_bytes, ai_gen_text
    except Exception as e:
        raise e

# Gradio UI
demo = gr.Interface(
    fn=process_audio,
    inputs=gr.Audio(sources=["microphone","upload"], type="numpy"),
    outputs= [
        gr.Audio(type="numpy", label="AI Response Audio"),
        gr.Textbox(label="AI Response Text")
    ],
    title="Speech-to-Text and AI Chat by Janak Mandavgade",
    description="Speak or upload an audio file, and get AI-generated responses.",
    flagging_mode='never'
)

app = gr.mount_gradio_app(app, demo, path="/")
#demo.launch()
