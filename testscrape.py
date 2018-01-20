from datetime import datetime
from bs4 import BeautifulSoup
import requests
import re



market_list = ['P','Q']
market_dic = {'P':'KOSPI', 'Q':'KOSDAQ'}

for market in market_list:
    print(market)
    industry = {}
    date = datetime.now().strftime('%Y%m%d')
    url = 'http://finance.daum.net/quote/all.daum?type=U&stype={}'.format(market)
    user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
    r = requests.get(url, headers= user_agent, auth=('user', 'pass'))
    soup = BeautifulSoup(r.text, 'html.parser')
    h4 = soup.findAll('h4', {'class':'fl_le'})
    # print(len(h4))
    table = soup.findAll('table',{'class':'gTable clr'})
    print(len(table))

    for i in range(len(h4)):
        sec = h4[i].text
        sec = re.sub('[0-9]','',sec)
        sec = re.sub('[-.%|]','',sec)
        industry[i] = sec

    data_list = []
    for i in range(len(industry)):
        td = table[i].findAll('td', {'class':'txt'})
        sector = industry[i]

        for t in td:
            ticker_inst = {}
            name = t.text
            a_tag = t.findAll('a')
            link = a_tag[0].attrs['href']
            code = link[-6:]
            # print(market_dic[market])
            # print(sector)
            ticker_inst = {'date':date,
                            'name':name,
                            'code':code,
                            'market_type':market_dic[market],
                            'sector':sector}
            data_list.append(ticker_inst)
    print(data_list)
    print(len(data_list))
