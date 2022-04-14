import logging
import datetime
import json
import requests
import nltk
from bs4 import BeautifulSoup
url = 'https://www.binance.com/en/blog/ecosystem/'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    series = [421499824684903686]
    url='https://www.binance.com/en/blog/ecosystem/'+str(series[0])
    r = requests.get(url)
    time_now = datetime.datetime.now()
    time = (time_now + datetime.timedelta(hours=15)).strftime("%Y-%m-%d %H:%M:%S")
    print(time)
    if r.status_code == 200:
        print(r.status_code)
        soup = BeautifulSoup(r.text, 'html.parser')
        title=soup.title.string
        app_data=soup.find('script',id='__APP_DATA')

        # app_data_json=app_data.json()
        # # print(app_data_json)
        # pageData=app_data_json['pageData']
        # redux=pageData['redux']
        # metaData=redux['metaData']
        # title=metaData['title']
        logger.info(title)
        # print(soup.prettify())
        # tokens=nltk.word_tokenize(title)
        # print(tokens)
        if 'invest' in title.lower():
            print('invest')
        else:
            print('no invest')
        coin=soup.find('div',{'class':'coin-name'})
        print(coin)
    else:
        logger.error('Error: %s', r.status_code)


if __name__ == '__main__':
    main()
