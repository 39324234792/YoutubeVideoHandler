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
    f = open("txtFiles/displayed.txt", "r", encoding="utf-8")
    textClips = []
    minLineLength = 50
    maxLineLength = 100
    for x in f:
        x = x.replace('\n', '')
        # if textClips is  empty
        if len(textClips) != 0:
            # if new  str + last entry in textClips is shorter that max length
            if len(x) + len(textClips[len(textClips)-1]) <= maxLineLength:
                newString = textClips[len(textClips)-1] + x
                textClips.pop()
                textClips.append(newString)
            # if last entry in textClips is shorter that min length
            elif len(textClips[len(textClips)-1]) >= maxLineLength:
                div = 1
                # find a point where the strings are longer than the minium
                while len(x[:math.floor(len(x)-div)]) + len(textClips[len(textClips)-1]) >= maxLineLength:
                    div += 1
                defict = 1
                while x[(math.floor(len(x)-div))-defict] != ' ':
                    defict += 1
                endStrDef = (math.floor(len(x)-div))-defict
                newString = textClips[len(textClips)-1] + x[:endStrDef]
                textClips.pop()
                textClips.append(newString)
                textClips = test(x[endStrDef:], textClips, minLineLength, maxLineLength)

            elif len(textClips[len(textClips) - 1]) >= maxLineLength:
                pass
            # if the string is too long
            elif len(x) >= maxLineLength:
                repStr = x
                while True:
                    appendableStr, leftover = textClipLenHandler(repStr, maxLineLength)
                    textClips.append(appendableStr)
                    if leftover is None:
                        break
                    repStr = leftover

            else:

                textClips.append(x)
        else:
            textClips.append(x)
    print(textClips)
    for i in textClips:
        print(len(i))


def test(x, textClips, minLineLength, maxLineLength):
    x = x.replace('\n', '')
    if len(textClips) != 0:
        if len(x) + len(textClips[len(textClips) - 1]) <= maxLineLength:
            newString = textClips[len(textClips) - 1] + x
            textClips.pop()
            textClips.append(newString)
            return textClips
        elif len(textClips[len(textClips) - 1]) <= minLineLength:
            div = 2
            print(len(x) / div)
            print(type(len(x) / div))
            while len(x[:math.floor(len(x) / div)]) + len(textClips[len(textClips) - 1]) <= minLineLength:
                div += 1
            newString = textClips[len(textClips) - 1] + x[:math.floor(len(x) / div)]
            textClips.pop()
            textClips.append(newString)
            textClips = test(x[math.floor(len(x) / div):], textClips, minLineLength, maxLineLength)

        else:
            textClips.append(x)
            return textClips
    else:
        textClips.append(x)
        return textClips


def textClipLenHandler(x, maxium):
    div = 1
    # find a point where the string is shorter than the max
    while len(x[:math.floor(len(x)-div)]) >= maxium:
        # as long as the string is longer than the max we add to div
        div += 1
    defict = 1
    while x[(math.floor(len(x) - div)) - defict] != ' ':
        defict += 1
    endStrDef = (math.floor(len(x) - div)) - defict
    newString = x[:endStrDef]
    leftoverStr  = x[endStrDef:]
    if len(leftoverStr) >= maxium:
        return newString, leftoverStr
    else:
        return newString, None


def getAudio():
    pass
    # audioHandler.audioGen("pass", "null")


getText()
# vidClipHandler()