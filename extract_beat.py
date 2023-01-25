import librosa
from midiutil.MidiFile import MIDIFile

# Function to extract beat from an audio file
def extract_beat(audio_file):
    # Load audio file
    y, sr = librosa.load(audio_file)

    # Extract beat frames
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    print("BPM:", tempo)
    # Convert beat frames to MIDI format
    midi_file = MIDIFile(1)
    track = 0
    time = 0
    midi_file.addTrackName(track, time, "Beat")
    midi_file.addTempo(track, time, int(tempo))

    for beat_frame in beat_frames:
        # Add a note to the MIDI file
        duration = 0.25
        velocity = 100
        pitch = 36
        midi_file.addNote(track, 0, pitch, beat_frame/sr, duration, velocity)
    # Export the MIDI file
    with open("beat.mid", "wb") as output_file:
        midi_file.writeFile(output_file)
    print(f"Beat from {audio_file} has been exported as beat.mid")

# Extract beat from an audio file
audio_file = "audio.mp3"
extract_beat(audio_file)
