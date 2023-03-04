import audioread


def duration_detector(length):
    hours = length // 3600  # calculate in hours
    length %= 3600
    mins = length // 60  # calculate in minutes
    length %= 60
    seconds = length  # calculate in seconds

    return hours, mins, seconds


def audioLen(file):
    with audioread.audio_open(file) as f:
        totalsec = f.duration
    print(totalsec)
    return totalsec
    # hours, mins, seconds = duration_detector(int(totalsec))
    # print('Total Duration: {}:{}:{}'.format(hours, mins, seconds))


def start(l):
    s = True
    for x in l:
        if s:
            s = False
        else:
            print(x)


dic = {
    'hello':"world",
    'bye': "earth"
}

print(str(list(dic.keys())[0]))