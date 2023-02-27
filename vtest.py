'''import os

from gtts import gTTS

# Options
text_to_read = "This is just a test using GTTS, a Python package library"
language = 'en'
slow_audio_speed = False
filename = 'audio_files/hello.mp3'

def reading_from_string():
    audio_created = gTTS(text=text_to_read, lang=language,
                         slow=slow_audio_speed)
    audio_created.save(filename)


def reading_from_file():
    f = open("txtFiles/displayed.txt", 'r')
    file_text = f.read()
    f.close()

    audio_created = gTTS(text=file_text, lang=language, slow=slow_audio_speed)
    audio_created.save(filename)


if __name__ == '__main__':
    reading_from_file()'''

import pyttsx3


def audioGen(name, text):
    # engine.setProperty('volume', 1.0)
    # voices = engine.getProperty('voices')  # getting details of current voice
    # engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
    engine.save_to_file(f'{text}', f'audio_files\\{name}.mp3')
    engine.runAndWait()


def fileRead(name):
    f = open("txtFiles/displayed.txt", 'r')
    file_text = f.read()
    f.close()
    engine.save_to_file(f'{file_text}', f'audio_files\\{name}.mp3')
    engine.say(f'{file_text}')
    engine.runAndWait()
    

if __name__ == '__main__':
    engine = pyttsx3.init()
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    engine.setProperty('voice', voice_id)
    engine.runAndWait()
    engine.setProperty('volume', 1.0)
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')

    for voice in voices:
        # to get the info. about various voices in our PC
        print("Voice:")
        print("ID: %s" % voice.id)
        print("Name: %s" % voice.name)
        print("Age: %s" % voice.age)
        print("Gender: %s" % voice.gender)
        print("Languages Known: %s" % voice.languages)
    fileRead('hello')
    #audioGen("tester", 'hello everyone')

'''import espeakng as espeak
espeak.espeak.init()
speaker = espeak.espeak.Espeak()
speaker.say("Hello world")
speaker.rate = 300
speaker.say("Faster hello world")'''

'''from TTS.api import TTS

# Running a multi-speaker and multi-lingual model

# List available TTS models and choose the first one
model_name = TTS.list_models()[6]
print(TTS.list_models())
# Init TTS
tts = TTS(model_name)
# Run TTS
# ❗ Since this model is multi-speaker and multi-lingual, we must set the target speaker and the language
# Text to speech with a numpy output
# wav = tts.tts("This is a test! This is also a test!!", speaker=tts.speakers[0], language=tts.languages[0])
# Text to speech to a file
tts.tts_to_file(text="Hello world!", speaker=tts.speakers[0], language=tts.languages[0], file_path="output.wav")'''

'''# Running a single speaker model

# Init TTS with the target model name
tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", progress_bar=False, gpu=False)
# Run TTS
tts.tts_to_file(text="Ich bin eine Testnachricht.", file_path=OUTPUT_PATH)

# Example voice cloning with YourTTS in English, French and Portuguese:
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=True)
tts.tts_to_file("This is voice cloning.", speaker_wav="my/cloning/audio.wav", language="en", file_path="output.wav")
tts.tts_to_file("C'est le clonage de la voix.", speaker_wav="my/cloning/audio.wav", language="fr", file_path="output.wav")
tts.tts_to_file("Isso é clonagem de voz.", speaker_wav="my/cloning/audio.wav", language="pt", file_path="output.wav")
'''



'''
import pyttsx3


def audioGen(name, text):
    engine = pyttsx3.init()
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')  # getting details of current voice
    engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
    engine.save_to_file(f'{text}', f'audio_files\\{name}.mp3')
    engine.runAndWait()


if __name__ == '__main__':
    engine = pyttsx3.init()
'''

'''rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')       # getting details of current voice
engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female
engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()
engine.save_to_file('Hello World', 'audio_files\\test.mp3')
engine.runAndWait()'''