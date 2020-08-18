import requests

payload = {
    "Audio": {
      "FileName":"recording.ogg"
    },
    "Video": {
      "FileName":"recording.webm"
    },
    "Transcript": {
      "FileName":"recording.srt"
    },
    "Output": {
      "FileName":"output.mkv"
    }

}


azurl = "https://saunbyffmpeg.azurewebsites.net/api/HttpJsonExample?code=tYKxHYMh36lOvMe6EfRw2FTGn2CP0htaahLvJ2c1JMzyO5r9qWHAkQ=="
lourl = 'http://localhost:7071/api/HttpJsonExample'
r = requests.post(azurl, json=payload)
print(r.status_code)
print(r.text)

azurl = "https://saunbyffmpeg.azurewebsites.net/api/HttpJsonFfmpegTranscript?code=tYKxHYMh36lOvMe6EfRw2FTGn2CP0htaahLvJ2c1JMzyO5r9qWHAkQ=="
lourl = 'http://localhost:7071/api/HttpJsonFfmpeg'
r = requests.post(azurl, json=payload)
print(r.status_code)
print(r.text)
