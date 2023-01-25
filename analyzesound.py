import os
import librosa

# specify the directory where the music files are located
directory = '/path/to/music/files'

# loop through all files in the directory
for filename in os.listdir(directory):
    # check if the file is a music file (e.g. .mp3, .wav, etc.)
    if filename.endswith('.mp3') or filename.endswith('.wav'):
        # load the music file
        y, sr = librosa.load(os.path.join(directory, filename))
        # extract the BPM
        bpm = librosa.beat.tempo(y=y, sr=sr)[0]
        # extract the key
        key = librosa.feature.tonnetz(y=y, sr=sr)
        # write the metadata to the file
        metadata = {'bpm': bpm, 'key': key}
        librosa.output.write_yaml(os.path.join(directory, filename), metadata)
