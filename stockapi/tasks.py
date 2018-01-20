from __future__ import absolute_import, unicode_literals
from celery.decorators import task
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import re
from stockapi.models import Ticker, OHLCV
import pandas as pd


@task(name="stock-ticker")
def stockticker():
    market_list = ['P','Q']
    market_dic = {'P':'KOSPI', 'Q':'KOSDAQ'}
    for market in market_list:
        print(market)
        success = False
        industry = {}
        data_list=[]
        date = datetime.now().strftime('%Y%m%d')
        url = 'http://finance.daum.net/quote/all.daum?type=U&stype={}'.format(market)
        user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
        r = requests.get(url, headers= user_agent, auth=('user', 'pass'))
        soup = BeautifulSoup(r.text, 'html.parser')
        h4 = soup.findAll('h4', {'class':'fl_le'})
        table = soup.findAll('table',{'class':'gTable clr'})

        for i in range(len(h4)):
            sec = h4[i].text
            sec = re.sub('[0-9]','',sec)
            sec = re.sub('[-.%|]','',sec)
            industry[i] = sec

        print(len(industry))
        for i in range(len(industry)):
            td = table[i].findAll('td', {'class':'txt'})
            sector = industry[i]
            for t in td:
                ticker_inst = {}
                name = t.text
                a_tag = t.findAll('a')
                link = a_tag[0].attrs['href']
                code = link[-6:]

                ticker_inst = Ticker(date=date,
                                    name=name,
                                    code=code,
                                    sector=sector,
                                    market_type=market_dic[market])
                data_list.append(ticker_inst)
        Ticker.objects.bulk_create(data_list)
        success = True
    return success


@task(name="ohlcv-get")
def ohlcv():
    success = False
    data_list = []
    today = datetime.now().strftime('%Y%m%d')
    ticker = Ticker.objects.filter(date=today)
    date_time = datetime.now().strftime('%Y%m%d%H%M%S')
    for i in range(len(ticker)):
        url = 'http://finance.naver.com/item/sise.nhn?code=' + ticker[i].code
        code = ticker[i].code
        user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
        r = requests.get(url, headers= user_agent, auth=('user', 'pass'))
        soup = BeautifulSoup(r.text, 'html.parser')
        name = soup.findAll('dt')[1].text
        df = pd.read_html(url, thousands='')

        name = name
        code = code
        date = date_time
        open_price = df[1].iloc[3,3].replace(",","")  #시가
        close_price = df[1].iloc[0,1].replace(",","") #현재가,종가
        high_price = df[1].iloc[4,3].replace(",","")  #고가
        low_price = df[1].iloc[5,3].replace(",","") #저가
        volume = df[1].iloc[3,1].replace(",","")

        ohlcv_inst = OHLCV(date=date, name=name, code=code,
                            open_price=open_price, close_price=close_price,
                            high_price=high_price, low_price=low_price,
                            volume=volume)

        data_list.append(ohlcv_inst)
        print(data_list)
    OHLCV.objects.bulk_create(data_list)
    success=True
    return success, "Data request complete"





# @task(name="kospi-ticker")
# def kospiticker():
#     # for market in market_list:
#     success = False
#     industry = {}
#     data_list=[]
#     date = datetime.now().strftime('%Y%m%d')
#     url = 'http://finance.daum.net/quote/all.daum?type=U&stype=P'
#     user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
#     r = requests.get(url, headers= user_agent, auth=('user', 'pass'))
#     soup = BeautifulSoup(r.text, 'html.parser')
#     h4 = soup.findAll('h4', {'class':'fl_le'})
#     table = soup.findAll('table',{'class':'gTable clr'})
#
#     for i in range(len(h4)):
#         sec = h4[i].text
#         sec = re.sub('[0-9]','',sec)
#         sec = re.sub('[-.%|]','',sec)
#         industry[i] = sec
#
#     for i in range(len(industry)):
#         td = table[i].findAll('td', {'class':'txt'})
#         sector = industry[i]
#         for t in td:
#             ticker_inst = {}
#             name = t.text
#             a_tag = t.findAll('a')
#             link = a_tag[0].attrs['href']
#             code = link[-6:]
#
#             ticker_inst = Ticker(date=date,
#                                 name=name,
#                                 code=code,
#                                 sector=sector,
#                                 market_type='KOSPI')
#             data_list.append(ticker_inst)
#     Ticker.objects.bulk_create(data_list)
#     success = True
#     return success
