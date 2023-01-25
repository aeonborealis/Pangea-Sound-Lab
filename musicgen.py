import librosa
from pydub import AudioSegment

# Function to adjust BPM and key of an audio file
def adjust_audio(audio_file, target_bpm, target_key):
    # Load audio file
    y, sr = librosa.load(audio_file)

    # Extract BPM and key
    bpm = librosa.beat.beat_track(y=y, sr=sr)[0]
    key = librosa.analyze.tonnetz(y=y, sr=sr)

    # Calculate BPM and key adjustment
    bpm_adjustment = target_bpm / bpm
    key_adjustment = target_key - key

    # Load audio file using pydub
    audio = AudioSegment.from_file(audio_file)

    # Adjust BPM
    audio_with_new_bpm = audio._spawn(audio.raw_data, overrides={"frame_rate": audio.frame_rate * bpm_adjustment})

    # Adjust key
    semitones = key_adjustment * 12
    audio_with_new_key = audio_with_new_bpm.pitch_shift(semitones)

    # Export adjusted audio file
    adjusted_audio_file = "adjusted_" + audio_file
    audio_with_new_key.export(adjusted_audio_file, format="mp3")
    print(f"{audio_file} has been adjusted to {target_bpm} BPM and {target_key} key and exported as {adjusted_audio_file}")
    return adjusted_audio_file

# Function to analyze and adjust audio files
def rework_audio(audio_file):
    # Load audio file
    y, sr = librosa.load(audio_file)

    # Analyze tempo and beat frames
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

    # Break audio file into chunks
    chunks = librosa.effects.split(y, beat_frames)

    # Adjust tempo and key of each chunk
    adjusted_chunks = []
    for chunk in chunks:
        adjusted_chunk = adjust_audio(chunk, tempo, key)
        adjusted_chunks.append(adjusted_chunk)

    # Concatenate chunks and export as new audio file
    reworked_audio = AudioSegment.empty()
    for chunk in adjusted_chunks:
        reworked_audio += AudioSegment.from_file(chunk)
    reworked_audio.export("reworked_audio.mp3", format="mp3")
    print("Reworked audio has been exported as reworked_audio.mp3")

# Rework audio files
audio1 = "audio1.mp3"
audio2 = "audio2.mp3"

rework_audio(audio1)
rework_audio(audio2)
