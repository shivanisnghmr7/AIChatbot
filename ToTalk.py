import requests
import uuid
import os
from dotenv import load_dotenv
load_dotenv()

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL"

headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": os.environ['ELEVEN_LABS_KEY']
}

def Text_to_Audio(text):
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }
    response = requests.post(url, json=data, headers=headers)
    
    # Generate a unique file path for the audio file
    audio_file_path = "/tmp/" + str(uuid.uuid4()) + '.mp3'
    
    # Save the audio file in chunks to the generated file path
    with open(audio_file_path, "wb") as audio_file:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                audio_file.write(chunk)

    # Return the path of the saved audio file
    return audio_file_path