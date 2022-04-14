import time
from threading import Event, Thread
from urllib import parse
import requests
import datetime
import json
from bs4 import BeautifulSoup
import logging

logging.basicConfig(filename='test.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.info('This message should go to the log file')
url = 'https://www.binance.com/en/support/announcement/c-157?navId=157'
Id_news = 89200
ID_support= 157


def get_latest():
    global Id_news
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

    }
    r = requests.get(url, headers=headers)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    app_data = soup.find('script', id='__APP_DATA')
    # print(app_data.text)
    data = json.loads(app_data.text)
    catalogs = data['routeProps']['b723']['catalogs']
    latest_news = None
    for each in catalogs:
        if each['catalogId'] == 49:
            latest_news = each
    articles = latest_news['articles']
    new_article = articles[0]
    if Id_news != new_article['id']:
        Id_news = new_article['id']
        print(new_article['title'])
        print('new infomation!')
        time_now = datetime.datetime.now()
        time = (time_now + datetime.timedelta(hours=15)).strftime("%Y-%m-%d %H:%M:%S")
        send(new_article['title'] + "\n送达时间:" + time)
        logging.info(new_article['title'] + "\n送达时间:" + time)


def get_support():
    global ID_support
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

    }
    r = requests.get(url, headers=headers)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    app_data = soup.find('script', id='__APP_DATA')
    # print(app_data.text)
    data = json.loads(app_data.text)
    catalogs = data['routeProps']['b723']['catalogs']
    Support = None
    for each in catalogs:
        if each['catalogId'] == 157:
            Support = each
    articles = Support['articles']
    new_article = articles[0]
    if ID_support != new_article['id']:
        ID_support = new_article['id']
        print(new_article['title'])
        print('new infomation!')
        time_now = datetime.datetime.now()
        time = (time_now + datetime.timedelta(hours=15)).strftime("%Y-%m-%d %H:%M:%S")
        send(new_article['title'] + "\n送达时间:" + time)
        logging.info(new_article['title'] + "\n送达时间:" + time)


def send(text):
    data = parse.urlencode({'text': text}).encode()
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': str(len(data))
    }
    url = "https://api.chanify.net/v1/sender/CICtqJYGEiJBQUxHVDJSS0hEMkJLQlFEQTZOS1dWVkRRWVc3TUNQR1lVIgYIAhoCd3U.JDPlA8aUcFYKYz2vnZNxgGKxzaf1fuDzR_jRalVsdzk"
    req = requests.post(headers=headers, url=url, data=data)


def call_repeatedly(interval, func, *args):
    stopped = Event()

    def loop():
        while not stopped.wait(interval):
            func(*args)

    Thread(target=loop).start()
    return stopped.set


def timer():
    print(datetime.datetime.now())


if __name__ == '__main__':
    print('start')
    call_repeatedly(1, get_support)
    call_repeatedly(1, timer)
    call_repeatedly(1, get_latest)
