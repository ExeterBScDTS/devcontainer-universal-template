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


def insights_to_srt(data, outStrings: [str]):
    index = 1
    for segment in data['videos'][0]['insights']['transcript']:
        start_time = format_time(segment['instances'][0]['start'])
        end_time = format_time(segment['instances'][0]['end'])
        text = segment['text']
        outStrings.append(f'{index}\n{start_time} --> {end_time}\n{text}\n\n')
        index += 1
    
