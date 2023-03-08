import requests
import json
import base64
import os
import shutil


def get_audio(text, voice='en_us_001', fullStr=False, reset=False):
    global fileNumber
    if reset:
        fileNumber = 0
    fileNumber += 1
    payload = {'text': text, 'voice': voice}
    payload = json.dumps(payload)
    r = requests.post(url, data=payload, headers={'Content-Type': 'application/json'})
    response = json.loads(r.text)
    if fullStr:
        wav_file = open(f"audio_files/complete/{fileNumber}.wav", "wb")
    else:
        wav_file = open(f"audio_files/{fileNumber}.wav", "wb")
    print(response)
    decodedData = base64.b64decode(response['data'])
    wav_file.write(decodedData)
    wav_file.close()
    if fullStr:
        return f"audio_files/complete/{fileNumber}.wav"
    return f"audio_files/{fileNumber}.wav"


def resetAudioFolder(path, clear=False):
    if clear:
        folder = path
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))


url = 'https://tiktok-tts.weilnet.workers.dev/api/generation'
fileNumber = 0