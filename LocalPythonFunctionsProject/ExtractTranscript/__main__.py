import logging

import json

def format_time(instance_time):
    mins_secs = instance_time.split(".")[0]
    try:
        millis = instance_time.split(".")[1]
    except IndexError:
        millis = "0"
    millis = float("." + millis)*1000
    return f'{mins_secs},{millis:03.0f}'
    

if __name__ == '__main__':
    with open('recording.ogg_insights.json', 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
        index = 1
        for segment in data['videos'][0]['insights']['transcript']:
            print(index)
            print(format_time(segment['instances'][0]['start']),'-->',format_time(segment['instances'][0]['end']))
            
            print(segment['text'])
            print()
            index += 1

