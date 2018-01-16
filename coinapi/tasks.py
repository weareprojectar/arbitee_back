from __future__ import absolute_import, unicode_literals
import random
import time
import requests
from celery.decorators import task
from datetime import datetime
from coinapi.models import Candle, Price

coins = ['BTC', 'ETH', 'BCC', 'ETC', 'XRP']

@task(name="scrape_upbit")
def scrape_upbit():
    success = False
    for coin in coins:
        user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
        url = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/minutes/1?code=CRIX.UPBIT.KRW-{}'.format(coin)
        r = requests.get(url, headers = user_agent, auth=('user', 'pass'))
        try:
            r = requests.get(url)
            while(r.status_code != 200):
                sec = random.random()
                time.sleep(sec)
                r = requests.get(url)
        except:
            print("status_code error")

        upbitdata = r.json()
        hi = upbitdata[0]['highPrice']
        lo = upbitdata[0]['lowPrice']
        op = upbitdata[0]['openingPrice']
        cl = upbitdata[0]['tradePrice']
        trp = upbitdata[0]['candleAccTradePrice']
        vol = upbitdata[0]['candleAccTradeVolume']
        mp = trp/vol
        date = datetime.fromtimestamp(int(upbitdata[0]['timestamp'])/1000).strftime("%Y-%m-%d %H:%M")
        ticker = coin

        record = Candle(date=date,
                           ticker=ticker,
                           hi=hi,
                           lo=lo,
                           op=op,
                           cl=cl,
                           trp = trp,
                           vol=vol,
                           mp=mp,)
        record.save()
        success = True
    return success, "Data request complete"


@task(name="scrape_upbit_price")
def scrape_data_pcice():
    success = False
    for coin in coins:
        url = 'https://crix-api-endpoint.upbit.com/v1/crix/trades/ticks?code=CRIX.UPBIT.KRW-{}'.format(coin)

        try:
            user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
            r = requests.get(url, headers = user_agent, auth=('user', 'pass'))
            while(r.status_code != 200):
                sec = random.random()
                time.sleep(sec)
                r = requests.get(url)
        except:
            print("status_code error!")

        ticker = coin
        upbitprice=r.json()
        date = datetime.fromtimestamp(int(upbitprice[0]['timestamp'])/1000).strftime("%Y-%m-%d %H:%M:%S.%f")
        price = upbitprice[0]['tradePrice']
        vol = upbitprice[0]['tradeVolume']
        prev_price = upbitprice[0]['prevClosingPrice']
        change = upbitprice[0]['change']
        ch_price = upbitprice[0]['changePrice']
        AB = upbitprice[0]['askBid']

        record = Price(date=date,
                        ticker=ticker,
                        price=price,
                        vol=vol,
                        prev_price=prev_price,
                        change=change,
                        ch_price=ch_price,
                        AB=AB,)

        record.save()
        success = True
    return success, "Data request complete"
