import urllib.request
import json


opener = urllib.request.build_opener(urllib.request.HTTPHandler())
urllib.request.install_opener(opener)
req = 'http://iss.moex.com/iss/history/engines/%(engine)s/markets/%(market)s/boards/%(board)s/securities.json?date=%(date)s'
params = {
    'engine': 'stock',
    'market': 'bonds',
    'board': 'TQOD',
    'date': '20210728'
}
url = req % params
print("url", url)
res = opener.open(url + '&start=0')
jres = json.load(res)
for data in jres['history']['data']:
    print(data)
