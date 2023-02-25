def clippers(x, clip, mLineLength):
    realMLineLength = mLineLength
    while x[mLineLength] != ' ':
        mLineLength -= 1
    clip.append(x[:mLineLength])
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