from playsound import playsound
from gtts import gTTS

def playaudio(audio):
playsound(audio)

def convert_to_audio(text):
audio = gTTS(text)
audio.save("test.mp3")
playaudio("Beijing_Bass.mp3")

convert_to_audio("hey Khaled") 
