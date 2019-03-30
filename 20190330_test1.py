from bs4 import BeautifulSoup
import requests
import os
import shutil


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

#示例地址：新浪新闻-政务模块
url = 'http://gov.sina.com.cn'

#通用下载方法
def download_jpg(image_url, image_localpath):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:    #当图片存在，返回状态码200，当图片不存在，则返回404，这里增加判断条件，防止程序假死
        with open(image_localpath, 'wb') as f:
            response.raw.deconde_content = True
            shutil.copyfileobj(response.raw, f)

#取得图片
def craw3(url):
    response = requests.get(url , headers = headers)
    soup = BeautifulSoup(response.text , 'lxml')
    for pic_href in soup.find_all('div' , class_ = 'banner_right fr'):    #先确定需要获取的图片的范围，即div名
        for pic in pic_href.find_all('img'):
            imgurl = pic.get('src')    #取得图片地址
            dir = os.path.abspath('.')
            filename = os.path.basename(imgurl)    #把图片链接前面地址去掉，只保留文件名称
            imgpath = os.path.join(dir, filename)    #把dir和filename做链接
            # http://a.com/b/c.jpg
            # /user/wilson/c.jpg
            print('开始下载 %s' % imgurl)
            download_jpg(imgurl, imgpath)

#下载单页图片
craw3(url)

#翻页示例，根据翻页时网址的变化规律总结而得出
#未实现多线程
#当翻页时网址没有变化时应如何实现？
# j = 0
# for i in range(12, 37, 12):
#     url = 'http://gov.sina.com.cn' + str(i)
#     j += 1
#     print('第 %d 页' % j)
#     craw3(url)

#tips：选中需要注释的代码，按 ctrl+/ 可快速注释多行代码