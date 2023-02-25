def clippers(x, clip, mLineLength):
    realMLineLength = mLineLength
    while x[mLineLength] != ' ':
        mLineLength -= 1
    clip.append(x[:mLineLength])
    print(x[:mLineLength])
    if len(x[mLineLength:]) >= realMLineLength:
        clip = clippers(x[mLineLength+1:], clip, realMLineLength)
    else:
        clip.append(x[mLineLength+1:])
    return clip


def clipText(f, maxLineLength):
    content = ''
    clips = []
    for x in f:
        x.strip()
        x = x.replace('\n', '')
        content += x
    return clippers(content, clips, maxLineLength)


'''import pyttsx3

def init():
    engine = pyttsx3.init()
    return engine


def audioGen(name, text):
    engine = pyttsx3.init()
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')  # getting details of current voice
    engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
    engine.save_to_file(f'{text}', f'audio_files\\{name}.mp3')
    engine.runAndWait()

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