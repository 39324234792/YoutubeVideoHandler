import requests
import json
import base64

url = 'https://tiktok-tts.weilnet.workers.dev/api/generation'
payload = {'text': 'omg this is so totally cool', 'voice': 'en_us_001'}
payload = json.dumps(payload)
r = requests.post(url, data=payload, headers={'Content-Type': 'application/json'})
print(r)
print(r.text)
print(type(r.text))
response = json.loads(r.text)
print(response)
print(type(response))
print(response['data'])

wav_file = open("audio_files/temp.wav", "wb")
decodedData = base64.b64decode(response['data'])
wav_file.write(decodedData)
wav_file.close()
