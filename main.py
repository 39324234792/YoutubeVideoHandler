from moviepy.editor import *
import TextHandler as txtHandler
import audioHandler
import moviepy.audio.AudioClip
import os
import random
import math


def videoS(audioClips, bgVid, short=True):
    charLimit = 30
    start = True
    newAudClips = []
    newAudDict = {}
    if short:
        for clip in audioClips:
            clips = []
            if start:
                start = False
            else:
                if len(audioClips[clip]) >= charLimit:
                    ret = txtHandler.clippers(audioClips[clip], clips, charLimit)
                    newAudClips.append('\n'.join(ret))
                else:
                    newAudClips.append(audioClips[clip])
        start = True
        x = 0
        for clip in audioClips:
            if start:
                newAudDict[clip] = audioClips[clip]
                start = False
            else:
                newAudDict[clip] = newAudClips[x]
                x += 1
        audioClips = newAudDict

    audioclip = AudioFileClip('audio_files/complete/final.wav')
    testVideoClip = VideoFileClip(bgVid)
    timestamp = math.floor(random.randint(1, testVideoClip.duration-audioclip.duration))
    print(timestamp)
    vidClips = []
    start = True

    for clip in audioClips:
        if start:
            start = False
        else:
            # print(clip)
            # print(audioClips[clip])
            audioclip = AudioFileClip(clip)
            leng = audioclip.duration - 0.25
            # print(leng)

            videoA = VideoFileClip(bgVid).subclip(timestamp, timestamp+leng)

            textA = TextClip(audioClips[clip], fontsize=30, color='white', font='Calibri-Bold')
            # , stroke_color='black', stroke_width=1.5
            text2A = textA.set_pos('center').set_duration(leng)

            video2A = CompositeVideoClip([videoA, text2A])
            timestamp += leng
            vidClips.append(video2A)

    videoC = concatenate_videoclips(vidClips)
    # audioclip = AudioFileClip(str(list(audioClips.keys())[0]))
    videoC = videoC.set_audio(audioclip)
    videoC.write_videofile(f'NewVideos/final.mp4')
    print(TextClip.list('font'))


def getText():
    f = open("txtFiles/holder.txt", "r", encoding="utf-8")
    maxLineLength = 50
    content, fullString, str = txtHandler.clipText(f, maxLineLength)
    # content.insert(0, fullString)
    for x in fullString:
        if x == '':
            fullString.remove(x)
    return content, fullString, str


def getAudio(content, fullString, str):
    audioHandler.resetAudioFolder('C:/Users/18043/PycharmProjects/test4/audio_files/complete', True)
    dict = {}
    fullDict = {}
    finalDict = {}
    for x in content:
       dict[audioHandler.get_audio(x, "en_us_007")] = x
    for x in fullString:
        fullDict[audioHandler.get_audio(x, "en_us_007", fullStr=True)] = x
    # if len(fullDict) > 1:
    #     finalDict[audioJoiner(dict)] = str
    # else:
    #     for x in fullDict:
    #         finalDict['audio_files/complete/final.wav'] = fullDict[x]

    finalDict[audioJoiner(fullDict)] = str

    for x in dict:
        finalDict[x] = dict[x]
    return finalDict


def audioJoiner(dict):
    clips = []
    for x in dict:
        clips.append(AudioFileClip(x))
    finalClip = moviepy.audio.AudioClip.concatenate_audioclips(clips)
    audioHandler.resetAudioFolder('C:/Users/18043/PycharmProjects/test4/audio_files/complete', True)
    finalClip.write_audiofile('audio_files/complete/final.wav')
    return 'audio_files/complete/final.wav'


def getInput():
    print("Welcome!!!")
    while True:
        try:
            short = int(input("Is the video a short, [1] for yes, [0] for no: "))
            break
        except ValueError:
            print("Not a valid answer, retry...")
    if short == 0:
        BGVideos = os.listdir('C:\\Users\\18043\\PycharmProjects\\test4\\BackgroundVideos\\long')
        short = False
    else:
        BGVideos = os.listdir('C:\\Users\\18043\\PycharmProjects\\test4\\BackgroundVideos\\short')
        short = True
    num = 0
    print('Background Videos:')
    for x in BGVideos:
        print(f'[{num}] {x}')
        num += 1
    while True:
        try:
            bgInput = int(input(""))
            break
        except ValueError:
            print("Not a Int, retry...")

    return BGVideos[bgInput], short


audios = [
    "en_us_001",
    "en_us_007",
    "en_au_001",
]
# contents = getText()
# getAudio(contents)
# vidClipHandler()
# txtClips, content, str = getText()
# videoS(getAudio(txtClips, content, str))
# print(getAudio(txtClips, content, str))
bgVideo, short = getInput()
txtClips, content, str = getText()
videoS(getAudio(txtClips, content, str), bgVideo, short=short)


