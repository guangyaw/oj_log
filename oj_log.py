
# import requests
from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
#
# i = 1
# ua=UserAgent();
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
#
# r = requests.get("https://oj.openedu.tw/status?myself=0&page=1", headers=headers)
# r.encoding = "utf8"
# soup = BeautifulSoup(r.text, "html.parser")
# print(soup)


from selenium import webdriver
import time
driver = webdriver.Chrome() # 如果你沒有把webdriver放在同一個資料夾中，必須指定位置給他
driver.get("https://oj.openedu.tw/status?myself=0&page=1")

time.sleep(5) # 等待javascript渲染出來，當然這個部分還有更進階的作法，關鍵字是implicit wait, explicit wait，有興趣可以自己去找
html = driver.page_source # 取得html文字
driver.close()  # 關掉Driver打開的瀏覽器

soup = BeautifulSoup(html, "html.parser")
tag_li =soup.find(attrs={"class": "ivu-table-body"})
print(tag_li)

tag_span = tag_li.find_all(["span", "a"])
print(tag_span)
y=1
for x in tag_span:
    if y%8 == 0:
        print(x.string)
        print()
    else:
        print(x.string)
    y = y+1


