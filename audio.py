import urllib.request
import json
import os
YND_OAUTH = '"'+os.environ['YND_OAUTH']+'"'
cmd = """curl -X POST \-H 'Content-Type: application/json' \-d '{"yandexPassportOauthToken": """+YND_OAUTH+"""}' \https://iam.api.cloud.yandex.net/iam/v1/tokens"""
os.system(cmd + " > " + "api.txt")
with open("api.txt", "r") as file:
    data = file.read()
    data  = data[16:][:-4]
FOLDER_ID = "b1grs9f7cacf81tr4vlc"
IAM_TOKEN = data
decodedData = ""

def start():
    global decodedData
    bashCommand = "ffmpeg -i message.ogg audio.wav"
    os.system(bashCommand)

    with open("audio.wav", "rb") as f:
        data = f.read()
        f.close()
    os.remove("audio.wav")
    os.remove("message.ogg")
    params = "&".join([
        "topic=general",
        "format=lpcm",
        "sampleRateHertz=48000",
        "folderId=%s" % FOLDER_ID,
        "lang=ru-RU"
    ])

    url = urllib.request.Request("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize/?%s" % params, data=data)
    url.add_header("Authorization", "Bearer %s" % IAM_TOKEN)
    url.add_header("Transfer-Encoding", "chunked")

    responseData = urllib.request.urlopen(url).read().decode('UTF-8')
    decodedData = json.loads(responseData)
    if decodedData.get("error_code") is None:
        return(decodedData.get("result"))
    