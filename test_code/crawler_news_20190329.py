from bs4 import BeautifulSoup
import requests

headers = {
    "Accept" :"text/html, application/xhtml+xml, application/xml;q=0.9,image/webq, */*;q=0.8",
    "Accept-Language": "zh-CN,zh; q=0.8",
    "Connection":"close",
    "Cookie":"_gauges_unique_hour = 1; _gauges_unique_day = 1; _gauges_unique_month = 1; _gauges_unique_year = 1;_gauges_unique = 1",

}

url = 'https://www.thepaper.cn'

#取得新闻标题
def craw2(url):
    response = requests.get(url, headers = headers)

    soup = BeautifulSoup(response.text, 'lxml')

    for title_href in soup.find_all('div', class = 'newsbox'):
        print([title.get('title')
               for title in title_href.find_all('a') if title.get('title')])

craw2(url)