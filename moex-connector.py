#!/usr/bin/env python
import random
import urllib.request
import json
import asyncio

# https://iss.moex.com/iss/reference/
# https://iss.moex.com/iss/engines/stock/markets/bonds/boards/

req = 'http://iss.moex.com/iss/history/engines/%(engine)s/markets/%(market)s/boards/%(board)s/securities.json?date=%(date)s'


async def run(date: int) -> None:
    global results

    opener = urllib.request.build_opener(urllib.request.HTTPHandler())
    urllib.request.install_opener(opener)
    params = {
        'engine': 'stock',
        'market': 'bonds',
        'board': 'TQOD',
        'date': str(date)
    }
    url = req % params
    print("url", url)
    res = opener.open(url + '&start=0')
    jres = json.load(res)
    # for data in jres['history']['data']:
    #     print(data)
    await asyncio.sleep(random.randint(1, 5))
    print(f"{date} finished")


async def main():
    await asyncio.gather(
        *[run(date) for date in range(20210720, 20210730)]
    )


asyncio.run(main())
