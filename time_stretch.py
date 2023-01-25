import librosa
import random

# Function to time stretch audio
def time_stretch(audio_file):
    # Load audio file
    y, sr = librosa.load(audio_file)

    # Generate a random stretch factor
    stretch_factor = random.uniform(0.5, 2)

    # Time stretch audio
    y_stretch = librosa.effects.time_stretch(y, sr, stretch_factor)

    # Export stretched audio
    librosa.output.write_wav("stretched_audio.wav", y_stretch, sr)
    print(f"Audio from {audio_file} has been stretched by a factor of {stretch_factor} and exported as stretched_audio.wav")

# Time stretch audio file
audio_file = "audio.mp3"
time_stretch(audio_file)
