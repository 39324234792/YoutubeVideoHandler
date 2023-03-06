from moviepy.editor import *
import TextHandler as txtHandler
import audioHandler


def videoS(audioClips, short=True):
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

    timestamp = 1
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

            videoA = VideoFileClip("BackgroundVideos/minecraftBG1.mp4").subclip(timestamp, timestamp+leng)

            textA = TextClip(audioClips[clip], fontsize=30, color='white', font='Calibri-Bold')
            # , stroke_color='black', stroke_width=1.5
            text2A = textA.set_pos('center').set_duration(leng)

            video2A = CompositeVideoClip([videoA, text2A])
            timestamp += leng
            vidClips.append(video2A)

    videoC = concatenate_videoclips(vidClips)
    audioclip = AudioFileClip(str(list(audioClips.keys())[0]))
    videoC = videoC.set_audio(audioclip)
    videoC.write_videofile(f'NewVideos/final.mp4')
    print(TextClip.list('font'))



    '''videoA = VideoFileClip("BackgroundVideos/minecraftBG2.mp4").subclip(1, 11)
    textA = TextClip("text 1", fontsize=50, color='white')
    text2A = textA.set_pos('center').set_duration(10)
    video2A = CompositeVideoClip([videoA, text2A])
    # video2A.write_videofile('NewVideos/text1.mp4')

    videoB = VideoFileClip("BackgroundVideos/minecraftBG2.mp4").subclip(11, 21)
    textB = TextClip("text 2", fontsize=50, color='white')
    text2B = textB.set_pos('center').set_duration(10)
    video2B = CompositeVideoClip([videoB, text2B])
    # video2B.write_videofile('NewVideos/text2.mp4')
    videoC = concatenate_videoclips([video2A, video2B])
    videoC.write_videofile('NewVideos/C.mp4')'''


def vidClipHandler(length, audioText):
    finalClips = []
    dictionary = dict(zip(audioText, length))
    for x in dictionary:
        pass


def getText():
    f = open("txtFiles/holder.txt", "r", encoding="utf-8")
    maxLineLength = 50
    content, fullString = txtHandler.clipText(f, maxLineLength)
    content.insert(0, fullString)
    return content


def getAudio(content):
    dict = {}
    for x in content:
        dict[audioHandler.get_audio(x, "en_us_007")] = x
    return dict


# def omg
# audioGen("test_audio", "Hello world")
audios = [
    "en_us_001",
    "en_us_007",
    "en_au_001",
]
# contents = getText()
# getAudio(contents)
# vidClipHandler()
videoS(getAudio(getText()))
