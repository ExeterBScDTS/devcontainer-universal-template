import requests

payload = {
    "Audio": {
      "FileName":"recording.ogg",
    }
}

r = requests.post('http://localhost:7071/api/HttpJsonExample', json=payload)
print(r.status_code)
print(r.text)