import numpy as np
from scipy.io.wavfile import read, write
from scipy.signal import resample

def arpeggiate_sound(file_name, bpm, scale):
    # Read the sound file
    rate, data = read(file_name)
    # Calculate the number of samples per beat at the given BPM
    samples_per_beat = rate / (bpm / 60)
    # Reshape the data to have one beat worth of samples in each row
    data = np.reshape(data, (-1, samples_per_beat))
    # Transpose the data so that each column represents one beat
    data = data.T
    # Create an empty array to hold the arpeggiated sound
    arpeggiated = np.array([])
    # Arpeggiate the sound by iterating through the columns
    # and adding the samples to the arpeggiated array
    for i, beat in enumerate(data):
        # Articulate the sound by only adding samples that match the scale
        if i % len(scale) in scale:
            arpeggiated = np.append(arpeggiated, beat)
    # Resample the sound to match the original rate
    arpeggiated = resample(arpeggiated, len(data.flatten()))
    # Write the arpeggiated sound to a new file
    write("arpeggiated_" + file_name, rate, arpeggiated)

# Example usage
arpeggiate_sound("original_sound.wav", 168, [0, 2, 4, 7])
