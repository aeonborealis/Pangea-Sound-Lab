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

# Analyze and adjust audio files
audio1 = "audio1.mp3"
audio2 = "audio2.mp3"

# Get target BPM and key
y1, sr1 = librosa.load(audio1)
target_bpm = librosa.beat.beat_track(y=y1, sr=sr1)[0]
target_key = librosa.analyze.tonnetz(y=y1, sr=sr1)

# Adjust audio files
adjusted_audio1 = adjust_audio(audio1, target_bpm, target_key)
adjusted_audio2 = adjust_audio(audio2, target_bpm, target_key)

# Concatenate and export the audio files
result = AudioSegment.from_file(adjusted_audio1) + AudioSegment.from_file(adjusted_audio2)
result.export("result.mp3", format="mp3")
