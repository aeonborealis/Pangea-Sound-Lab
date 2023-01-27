from pydub import AudioSegment
from pydub.effects import arpeggio

def arpeggiate_sound(sound_path:str)->None:
    sound = AudioSegment.from_file(sound_path)
    arp = arpeggio(sound, tempo=120)
    arp.export("arpeggiated_sound.wav", format="wav")

arpeggiate_sound("path/to/sound.wav")
