import numpy as np
from scipy.io.wavfile import read, write

def sequence_sound(file_name, bpm):
  # Read the sound file
  rate, data = read(file_name)
  # Calculate the number of samples per beat at the given BPM
  samples_per_beat = rate / (bpm / 60)
  # Reshape the data to have on beat worth of samples in each row
  data = np.reshape(data, (-1, samples_per_beat))
  # Transpose the data so that each column represents one beat 
  data = data.T
  # Flatten the data back into a single array 
  data = data.flatten()
  # Write the sequence to a new sound file 
  write("sequenced_" + file_name, rate, data)
  
# Example usage
sequence_sound("original_sound.wave", 168)
