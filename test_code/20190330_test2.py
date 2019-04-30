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

#示例地址：新浪图片体育汇集
url = 'http://slide.sports.sina.com.cn'

#js完整路径
#http://slide.sports.sina.com.cn/js/v1/default/category.js

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
    for pic_href in soup.find_all('div' , class_ = 'hd'):    #先确定需要获取的图片的范围，即div名
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
#craw3(url)

#js实现的翻页，url不变化的情况

def get_page(url,page_num):
    pageList =[]
    for i in range(1,page_num +1):
        formdata ={'type':'index' ,
                   'paged': i}
        try:
            r = requests.post(url,data =formdata)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            print('链接成功')
            p = re.compile(r'href="(http://www.jdlingyu.net/\d{5}/)"')
            tempList = re.findall(p,r.text)
            for each in tempList:
                pageList.append(each)
                print('保存页面成功')
            tempList = []
        except:
            print('链接失败')
    print(pageList)
    return pageList