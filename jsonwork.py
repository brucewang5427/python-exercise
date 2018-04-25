import json
import sys

import pyperclip
import requests

if len(sys.argv) > 1:
    location = ' '.join(sys.argv[1:])
else:
    location = pyperclip.paste()
try:
    appid = 'ede8a254fa92d83126f6fe89e04e2117'
    url = 'http://samples.openweathermap.org/data/2.5/forecast?q={0}&appid={1}'.format(location, appid)
    res = requests.get(url)
    res.raise_for_status()
    weatherdata = json.loads(res.text)
    w = weatherdata['list']
    print('Current weather in {}: '.format(location))
    print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
    print()
    print('Tomorrow: ')
    print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
    print('Day after tomorrow: ')
    print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
except Exception as ex:
    print(ex)
