html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elise" class="sister" id = "link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id = "link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id = "link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class=story">...</p>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc,'lxml')
print(soup.prettify())

#找到title标签
print(soup.title)

#title标签里的内容
print(soup.title.string)

print(soup.a)

#找到所有的a标签
print(soup.find_all('a'))

print(soup.p)

print(soup.find(id="link3"))