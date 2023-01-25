import random
import numpy as np
from scipy.io.wavfile import read, write

def glitch_sound(file_name):
    # Read the sound file
    rate, data = read(file_name)
    # Generate random noise to add to the sound
    noise = np.random.normal(0, 1, data.shape)
    # Scramble some parts of the sound by randomly swapping samples
    for _ in range(1000):
        i, j = random.randint(0, len(data)), random.randint(0, len(data))
        data[i], data[j] = data[j], data[i]
    # Add the noise to the sound
    data = data + noise
    # Write the glitched sound to a new file
    write("glitched_" + file_name, rate, data)

# Example usage
glitch_sound("original_sound.wav")
