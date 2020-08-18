import requests

payload = {
    "Insights": {
      "FileName":"recording.ogg_insights.json"
    },
    "Transcript": {
      "FileName":"recording.srt"
    }

}

azurl = "https://saunbyffmpeg.azurewebsites.net/api/HttpJsonExample?code=tYKxHYMh36lOvMe6EfRw2FTGn2CP0htaahLvJ2c1JMzyO5r9qWHAkQ=="
lourl = 'http://localhost:7071/api/HttpJsonExample'
r = requests.post(lourl, json=payload)
print(r.status_code)
print(r.text)

azurl = "https://saunbyffmpeg.azurewebsites.net/api/HttpJsonTranscript?code=tYKxHYMh36lOvMe6EfRw2FTGn2CP0htaahLvJ2c1JMzyO5r9qWHAkQ=="
lourl = 'http://localhost:7071/api/HttpJsonTranscript'
r = requests.post(lourl, json=payload)
print(r.status_code)
print(r.text)

#azurl = "https://saunbyffmpeg.azurewebsites.net/api/HttpJsonBlobExample?code=tYKxHYMh36lOvMe6EfRw2FTGn2CP0htaahLvJ2c1JMzyO5r9qWHAkQ=="
#lourl = 'http://localhost:7071/api/HttpJsonBlobExample'
#r = requests.post(lourl, json=payload)
#print(r.status_code)
#print(r.text)