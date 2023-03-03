import audioread


def duration_detector(length):
    hours = length // 3600  # calculate in hours
    length %= 3600
    mins = length // 60  # calculate in minutes
    length %= 60
    seconds = length  # calculate in seconds

    return hours, mins, seconds


with audioread.audio_open('1.wav') as f:
    totalsec = f.duration
    print(totalsec)
    # hours, mins, seconds = duration_detector(int(totalsec))
    # print('Total Duration: {}:{}:{}'.format(hours, mins, seconds))
