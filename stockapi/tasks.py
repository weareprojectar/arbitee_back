from __future__ import absolute_import, unicode_literals
from celery.decorators import task
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import re
from stockapi.models import Ticker, OHLCV, STOCKINFO
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

def ohlcv(ticker):
    success = False
    data_list = []
    date_time = datetime.now().strftime('%Y%m%d')
    for i in range(len(ticker)):
        url = 'http://finance.naver.com/item/sise.nhn?code=' + ticker[i].code
        code = ticker[i].code
        user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
        r = requests.get(url, headers= user_agent, auth=('user', 'pass'))
        soup = BeautifulSoup(r.text, 'html.parser')
        name = soup.findAll('dt')[1].text
        df = pd.read_html(url, thousands='')
        market = ticker[i].market_type
        name = name
        code = code
        date = date_time
        open_price = df[1].iloc[3,3].replace(",","")  #시가
        close_price = df[1].iloc[0,1].replace(",","") #현재가,종가
        high_price = df[1].iloc[4,3].replace(",","")  #고가
        low_price = df[1].iloc[5,3].replace(",","") #저가
        volume = df[1].iloc[3,1].replace(",","")

        ohlcv_inst = OHLCV(date=date, name=name, code=code, market_type=market,
                            open_price=open_price, close_price=close_price,
                            high_price=high_price, low_price=low_price,
                            volume=volume)

        data_list.append(ohlcv_inst)
    OHLCV.objects.bulk_create(data_list)
    success=True
    return success, "Data request complete"

def stockinfo(ticker):
    success =False
    m_status = []
    for i in range(len(ticker)):
        url = 'http://finance.naver.com/item/sise.nhn?code=' + ticker[i].code
        user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
        r = requests.get(url, headers= user_agent, auth=('user', 'pass'))
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        soup = BeautifulSoup(r.text, 'html.parser')
        name = soup.findAll('dt')[1].text
        code = ticker[i].code
        market_type = ticker[i].market_type
        market_data = soup.find('div', {'class':'rate_info'})
        market_status = market_data.findAll('span',{'class':'blind'})[0].text
        df = pd.read_html(url, thousands='')
        volume=df[0].iloc[0,2].split(" ")[-1]
        status = STOCKINFO(date=date, code=code, name=name, price=market_status.replace(',',''), market_type=market_type, volume=volume.replace(',',''))
        m_status.append(status)
    STOCKINFO.objects.bulk_create(m_status)
    success=True
    return success


@task(name="ohlcv-get-01")
def ohlcv_1():
    today = datetime.now().strftime('%Y%m%d')
    ticker = Ticker.objects.filter(date=today).order_by('id')
    ticker_count = ticker.count()
    ticker_cut = ticker_count//10
    ticker_list = ticker[:ticker_cut]
    ohlcv(ticker_list)

@task(name="ohlcv-get-02")
def ohlcv_2():
    today = datetime.now().strftime('%Y%m%d')
    ticker = Ticker.objects.filter(date=today).order_by('id')
    ticker_count = ticker.count()
    ticker_cut = ticker_count//10
    ticker_list = ticker[ticker_cut:2*ticker_cut]
    ohlcv(ticker_list)

@task(name="ohlcv-get-03")
def ohlcv_3():
    today = datetime.now().strftime('%Y%m%d')
    ticker = Ticker.objects.filter(date=today).order_by('id')
    ticker_count = ticker.count()
    ticker_cut = ticker_count//10
    ticker_list = ticker[2*ticker_cut:3*ticker_cut]
    ohlcv(ticker_list)

@task(name="ohlcv-get-04")
def ohlcv_4():
    today = datetime.now().strftime('%Y%m%d')
    ticker = Ticker.objects.filter(date=today).order_by('id')
    ticker_count = ticker.count()
    ticker_cut = ticker_count//10
    ticker_list = ticker[3*ticker_cut:4*ticker_cut]
    ohlcv(ticker_list)

@task(name="ohlcv-get-05")
def ohlcv_5():
    today = datetime.now().strftime('%Y%m%d')
    ticker = Ticker.objects.filter(date=today).order_by('id')
    ticker_count = ticker.count()
    ticker_cut = ticker_count//10
    ticker_list = ticker[4*ticker_cut:5*ticker_cut]
    ohlcv(ticker_list)

@task(name="ohlcv-get-06")
def ohlcv_6():
    today = datetime.now().strftime('%Y%m%d')
    ticker = Ticker.objects.filter(date=today).order_by('id')
    ticker_count = ticker.count()
    ticker_cut = ticker_count//10
    ticker_list = ticker[5*ticker_cut:6*ticker_cut]
    ohlcv(ticker_list)

@task(name="ohlcv-get-07")
def ohlcv_7():
    today = datetime.now().strftime('%Y%m%d')
    ticker = Ticker.objects.filter(date=today).order_by('id')
    ticker_count = ticker.count()
    ticker_cut = ticker_count//10
    ticker_list = ticker[6*ticker_cut:7*ticker_cut]
    ohlcv(ticker_list)

@task(name="ohlcv-get-08")
def ohlcv_8():
    today = datetime.now().strftime('%Y%m%d')
    ticker = Ticker.objects.filter(date=today).order_by('id')
    ticker_count = ticker.count()
    ticker_cut = ticker_count//10
    ticker_list = ticker[7*ticker_cut:8*ticker_cut]
    ohlcv(ticker_list)

@task(name="ohlcv-get-09")
def ohlcv_9():
    today = datetime.now().strftime('%Y%m%d')
    ticker = Ticker.objects.filter(date=today).order_by('id')
    ticker_count = ticker.count()
    ticker_cut = ticker_count//10
    ticker_list = ticker[8*ticker_cut:9*ticker_cut]
    ohlcv(ticker_list)

@task(name="ohlcv-get-10")
def ohlcv_10():
    today = datetime.now().strftime('%Y%m%d')
    ticker = Ticker.objects.filter(date=today).order_by('id')
    ticker_count = ticker.count()
    ticker_cut = ticker_count//10
    ticker_list = ticker[9*ticker_cut:]
    ohlcv(ticker_list)

@task(name="stock-get-01")
def stock_1():
    today = datetime.now().strftime('%Y%m%d')
    ticker = Ticker.objects.filter(date=today).order_by('id')
    ticker_count = ticker.count()
    ticker_cut = ticker_count//10
    ticker_list = ticker[:ticker_cut]
    stockinfo(ticker_list)

@task(name="stock-get-02")
def stock_2():
    today = datetime.now().strftime('%Y%m%d')
    ticker = Ticker.objects.filter(date=today).order_by('id')
    ticker_count = ticker.count()
    ticker_cut = ticker_count//10
    ticker_list = ticker[ticker_cut:2*ticker_cut]
    stockinfo(ticker_list)

@task(name="stock-get-03")
def stock_3():
    today = datetime.now().strftime('%Y%m%d')
    ticker = Ticker.objects.filter(date=today).order_by('id')
    ticker_count = ticker.count()
    ticker_cut = ticker_count//10
    ticker_list = ticker[2*ticker_cut:3*ticker_cut]
    stockinfo(ticker_list)

@task(name="stock-get-04")
def stock_4():
    today = datetime.now().strftime('%Y%m%d')
    ticker = Ticker.objects.filter(date=today).order_by('id')
    ticker_count = ticker.count()
    ticker_cut = ticker_count//10
    ticker_list = ticker[3*ticker_cut:4*ticker_cut]
    stockinfo(ticker_list)

@task(name="stock-get-05")
def stock_5():
    today = datetime.now().strftime('%Y%m%d')
    ticker = Ticker.objects.filter(date=today).order_by('id')
    ticker_count = ticker.count()
    ticker_cut = ticker_count//10
    ticker_list = ticker[4*ticker_cut:5*ticker_cut]
    stockinfo(ticker_list)

@task(name="stock-get-06")
def stock_6():
    today = datetime.now().strftime('%Y%m%d')
    ticker = Ticker.objects.filter(date=today).order_by('id')
    ticker_count = ticker.count()
    ticker_cut = ticker_count//10
    ticker_list = ticker[5*ticker_cut:6*ticker_cut]
    stockinfo(ticker_list)

@task(name="stock-get-07")
def stock_7():
    today = datetime.now().strftime('%Y%m%d')
    ticker = Ticker.objects.filter(date=today).order_by('id')
    ticker_count = ticker.count()
    ticker_cut = ticker_count//10
    ticker_list = ticker[6*ticker_cut:7*ticker_cut]
    stockinfo(ticker_list)

@task(name="stock-get-08")
def stock_8():
    today = datetime.now().strftime('%Y%m%d')
    ticker = Ticker.objects.filter(date=today).order_by('id')
    ticker_count = ticker.count()
    ticker_cut = ticker_count//10
    ticker_list = ticker[7*ticker_cut:8*ticker_cut]
    stockinfo(ticker_list)

@task(name="stock-get-09")
def stock_9():
    today = datetime.now().strftime('%Y%m%d')
    ticker = Ticker.objects.filter(date=today).order_by('id')
    ticker_count = ticker.count()
    ticker_cut = ticker_count//10
    ticker_list = ticker[8*ticker_cut:9*ticker_cut]
    stockinfo(ticker_list)

@task(name="stock-get-10")
def stock_10():
    today = datetime.now().strftime('%Y%m%d')
    ticker = Ticker.objects.filter(date=today).order_by('id')
    ticker_count = ticker.count()
    ticker_cut = ticker_count//10
    ticker_list = ticker[9*ticker_cut:]
    stockinfo(ticker_list)

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
