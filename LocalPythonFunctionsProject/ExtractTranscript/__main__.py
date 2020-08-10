import logging

import json

if __name__ == '__main__':
    with open('recording.ogg_insights.json', 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
        for segment in data['videos'][0]['insights']['transcript']:
            print(segment['text'])

