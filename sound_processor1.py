import os
import random
import librosa
import numpy as np
from scipy.signal import resample

# specify the directory where the music files are located
directory = '/path/to/music/files'

# initialize an empty list to hold the audio data
audio_data = []

# loop through all files in the directory
for filename in os.listdir(directory):
    # check if the file is a music file (e.g. .mp3, .wav, etc.)
    if filename.endswith('.mp3') or filename.endswith('.wav'):
        # load the music file
        y, sr = librosa.load(os.path.join(directory, filename))
        # scramble the audio data
        y = y[random.sample(range(len(y)), len(y))]
        # time stretch the audio data
        stretch_factor = random.uniform(0.5, 2)
        y = librosa.effects.time_stretch(y, stretch_factor)
        # arpeggiate the audio data
        y = librosa.effects.arpeggiate(y, sr, intervals=[1.618])
        # add the audio data to the list
        audio_data.append(y)

# concatenate the audio data
audio_data = np.concatenate(audio_data)

# resample the audio data to a common sampling rate
target_sr = 44100
audio_data = resample(audio_data, int(len(audio_data) * target_sr / sr))

# write the audio data to a new file
librosa.output.write_wav('output.wav', audio_data, target_sr)
