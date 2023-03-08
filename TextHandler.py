def clippers(x, clip, mLineLength):
    realMLineLength = mLineLength
    if mLineLength > len(x):
        mLineLength = len(x) - 1

    while True:
        if x[mLineLength] == ' ' or x[mLineLength] == '.':
            break
        else:
            mLineLength -= 1

    clip.append(x[:mLineLength+1])
    if len(x[mLineLength:]) >= realMLineLength:
        clip = clippers(x[mLineLength+1:], clip, realMLineLength)
    else:
        clip.append(x[mLineLength+1:])
    return clip


def clipText(f, maxLineLength):
    content = ''
    clips = []
    clips2 = []
    for x in f:
        x.strip()
        x = x.replace('\n', '')
        content += x

    return clippers(content, clips, maxLineLength), clippers(content, clips2, 250), content