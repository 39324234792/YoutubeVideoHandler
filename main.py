import moviepy.editor as mp
# import vtest as audioHandler
import math
import TextHandler as TxtHandler


def video(audio=None):
    clip = mp.VideoFileClip("BackgroundVideos/scaryBGTrim.mp4")

    txt_clip = mp.TextClip("GeeksforGeeks", fontsize=75, color='white')
    txt = mp.TextClip("GoodGeeks ", fontsize=75, color='white')

    txt_clip = txt_clip.set_pos('center').set_duration(0, 10)
    txt_clip2 = txt.set_pos('left').set_duration(10, 30)
    final_clip = mp.CompositeVideoClip([clip, txt_clip, txt_clip2])
    final_clip.write_videofile("my_new_video.mp4")
    final_clip.close()


def vidClipHandler(length, audioText):
    finalClips = []
    dictionary = dict(zip(audioText, length))
    for x in dictionary:
        pass


def getText():
    f = open("txtFiles/holder.txt", "r", encoding="utf-8")
    maxLineLength = 100
    content = TxtHandler.clipText(f, maxLineLength)
    for x in content:
        print(x)


def getAudio():
    pass
    # audioHandler.audioGen("pass", "null")


getText()
# vidClipHandler()