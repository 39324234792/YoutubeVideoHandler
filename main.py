from moviepy.editor import *
import TextHandler as TxtHandler
import audioHandler


def videoS(audio=None):
    videoA = VideoFileClip("BackgroundVideos/minecraftBG2.mp4").subclip(1, 11)
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
    videoC.write_videofile('NewVideos/C.mp4')


def vidClipHandler(length, audioText):
    finalClips = []
    dictionary = dict(zip(audioText, length))
    for x in dictionary:
        pass


def getText():
    f = open("txtFiles/holder.txt", "r", encoding="utf-8")
    maxLineLength = 50
    content = TxtHandler.clipText(f, maxLineLength)
    for x in content:
        print(x)
    return content


def getAudio(content):
    dict = {}
    for x in content:
        dict[audioHandler.get_audio(x)] = x
    print(dict)

    return dict


# audioGen("test_audio", "Hello world")
# contents = getText()
# getAudio(contents)
# vidClipHandler()
videoS()