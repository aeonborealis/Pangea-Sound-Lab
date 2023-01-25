import random
import wave

def shuffle_sound(file_name):
    # Open the sound file
    with wave.open(file_name, "rb") as sound:
        # Read the frames from the sound file
        frames = sound.readframes(sound.getnframes())
        # Convert the frames to a list
        frames = list(frames)
        # Shuffle the frames in random order 
        random.shuffle(frames)
        # Create a new sound file with the same parameters as the original
        with wave.open("shuffled_"+file_name, "wb") as shuffled_sound:
            shuffled_sound.setparams(sound.getparams())
            # Write the shuffled frames to the new sound file
            shuffled_sound.writeframes(bytes(frames))

# Example Usage
shuffle_sound("original_sound.wav")
