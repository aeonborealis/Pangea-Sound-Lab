import librosa
import numpy as np
import random
from pydub import AudioSegment

# Function to extract parts of dynamic interest from an audio file
def extract_dynamic_parts(audio_file):
    # Load audio file
    y, sr = librosa.load(audio_file)

    # Extract dynamic features
    rms = librosa.feature.rms(y=y)
    dynamic_parts = librosa.effects.split(y, top_db=np.max(rms) - 30)

    # Scramble dynamic parts
    random.shuffle(dynamic_parts)

    # Concatenate scrambled dynamic parts
    dynamic_audio = np.concatenate(dynamic_parts)

    # Export scrambled dynamic audio
    librosa.output.write_wav("scrambled_dynamic_audio.wav", dynamic_audio, sr)
    print(f"Dynamic parts from {audio_file} have been extracted and scrambled as scrambled_dynamic_audio.wav")

# Extract dynamic parts from an audio file
audio_file = "audio.mp3"
extract_dynamic_parts(audio_file)
