import librosa
import numpy as np
from midiutil.MidiFile import MIDIFile

# Function to extract melody from an audio file
def extract_melody(audio_file):
    # Load audio file
    y, sr = librosa.load(audio_file)

    # Extract melody using the CQT (Constant-Q Transform)
    cqt = librosa.cqt(y, sr=sr)
    melody = np.argmax(cqt, axis=0)

    # Convert melody to MIDI format
    midi_file = MIDIFile(1)
    track = 0
    time = 0
    midi_file.addTrackName(track, time, "Melody")
    midi_file.addTempo(track, time, 120)

    for pitch in melody:
        # Add a note to the MIDI file
        duration = 1
        velocity = 100
        midi_file.addNote(track, 0, pitch, time, duration, velocity)
        time += duration

    # Export the MIDI file
    with open("melody.mid", "wb") as output_file:
        midi_file.writeFile(output_file)
    print(f"Melody from {audio_file} has been exported as melody.mid")

# Extract melody from an audio file
audio_file = "audio.mp3"
extract_melody(audio_file)
