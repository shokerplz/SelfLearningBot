import urllib.request
import json
import os

FOLDER_ID = "b1grs9f7cacf81tr4vlc"
IAM_TOKEN = "CggaATEVAgAAABKABJDpOzeWvEhznNidlPxL198zRLNYXKKttwTexz_Influsu3aFHbAxz3qHDe7l2ef1L085WqQCZxYk5hNZRIxcH5rPL3GublOM-jcKFL8RsI7g1yZ9Llihik2qe2z6Z6TpttkYr4jzQF_uEaiY9cGjKbwBdS_UfHaxuL44E0TRse5o7oihSoQipamYRnuiGnnn6mKQ3Kn_ogIu8Ljxe3uOHO0uTVYqs4c7-pVb4X1LbjRfIMtQUCZJt9UZVre-Q9vLyDiM9PRz8V54z-Qis2SZ3J68ir-lOfsm7pKXleG6HmrX3ViYFzxdH0QFoQXYyCWcaqsFn0nTLmwyvsnvqUz7ynQ1lEIT9u3FwkXabwFTLVwrJjHIZ0h_n8rfQr6BaUTSxvPXYxoAEp70kfiHgYtgSbboMeH2xiTDKi7nxALCXfSSUgH-gqxCRp-cZC6bCb2I0XcgNQ1TjMxYTWFDsWK172FBxwX8RtQ30USgPulcDW__L43O_cX9Gk3sJLG2_WbzaJwBpX9j1mhNZosK3RHwM2lQ0Sz1uUgs4oUk4xZ585gIvUTPCm3Rcp1WSXqcZjOEN2CpLClY5l3TwaReskB-5FAzCEMz9rl1a8lbjbfqg3gfbxdERSPuidjWm0UzO8xhCMw2blS4LMZ0Gl7cOk9Su3yU69r9QQDMhw6h_D5kbMnGmcKIGM2N2YyZTM4NzQxZTQ0YmNhZjc2OWEzYTk4ZTIzMzFiEN674OIFGJ6N4-IFIiUKFGFqZTFtaWM1NXRsdXVwaWtzMTFtEg1pdmFuLmtvdmFsZXY1WgAwAjgBSggaATEVAgAAAFABIPYE"
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
    