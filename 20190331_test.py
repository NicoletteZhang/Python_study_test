import requests
import os
import re

#定义headers
headers = {
    "Accept" :"text/html, application/xhtml+xml, application/xml;q=0.9,image/webq, */*;q=0.8",
    "Accept-Language": "zh-CN,zh; q=0.8",
    "Connection":"close",
    "Cookie":"_gauges_unique_hour = 1; _gauges_unique_day = 1; _gauges_unique_month = 1; _gauges_unique_year = 1;_gauges_unique = 1",
    "Referer":"https://news.sina.com.cn",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 Edge/15.15063"
}

url = 'http://www.jdlingyu.mobi/'

root = '/Users/Nicolette/Pictures/绝对领域'

#在分析网页源代码上还不够熟练，不能很快定位类名、关键变量名等
def get_page(url, page_num):
    pageList = []
    for i in range(1, page_num + 1):
        formdata = {'type': 'index',
                    'paged': i}
        try:
            r = requests.post(url, data=formdata)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            print('链接成功')
            p = re.compile(r'href="(http://www.jdlingyu.mobi/\d{5}/)"')
            tempList = re.findall(p, r.text)
            for each in tempList:
                pageList.append(each)
                print('保存页面成功')
            tempList = []
        except:
            print('链接失败')
    print(pageList)
    return pageList


def get_picure(pageList):
    picList = []
    for each in pageList:
        try:
            r = requests.get(each, headers = headers)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            p = re.compile('http://img.jdlingyu.mobi/[^"]+\.jpg|http://w[wx][23].sinaimg.cn/[^"]+\.jpg')
            tempList = re.findall(p, r.text)
            for each in tempList:
                picList.append(each)
                print('保存图片链接成功')
            tempList = []
        except:
            print('保存图片链接失败')
    return picList


def down_picture(picList, root):
    picList = list(set(picList))
    if not os.path.exists(root):
        os.mkdir(root)
    for each in picList:
        path = root + each.split('/')[-1]
        if not os.path.exists(path):
            r = requests.get(each, headers=headers)
            r.raise_for_status()
            with open(path, 'wb') as f:
                f.write(r.content)
                print('动图已保存')
        else:
            print('动图已存在')


pageList = get_page(url, 2)
picList = get_picure(pageList)
down_picture(picList, root)
