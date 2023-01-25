import librosa
import random
from pydub import AudioSegment
from tkinter import *

# Function to randomly combine audio files
def combine_audio():
    # Get list of audio files
    audio_files = ["audio1.mp3", "audio2.mp3", "audio3.mp3"]

    # Randomly select two audio files
    audio1 = random.choice(audio_files)
    audio2 = random.choice(audio_files)

    # Load audio files using pydub
    audio1 = AudioSegment.from_file(audio1)
    audio2 = AudioSegment.from_file(audio2)

    # Generate random offset
    offset = random.randint(0, len(audio1) - len(audio2))

    # Combine audio files
    combined_audio = audio1.overlay(audio2, position=offset)

    # Export combined audio
    combined_audio.export("combined_audio.mp3", format="mp3")
    print("Audio files have been combined and exported as combined_audio.mp3")

# Create GUI
root = Tk()
root.title("Audio Combiner")

combine_button =
