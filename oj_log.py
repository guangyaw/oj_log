
# import requests
from bs4 import BeautifulSoup
import csv
from pyvirtualdisplay import Display
from selenium import webdriver
import time

display = Display(visible=0, size=(640, 480))
display.start()

page = 2
target_list = [[0 for i in range(8)] for j in range(12*page)]
m = 0
for z in range(page):
    m = z*12
    print("m="+str(m))
    driver = webdriver.Chrome("/home/xyaw/PycharmProjects/oj_log/chromedriver")  # 把webdriver放在此路徑（可自訂）
    driver.get("https://oj.openedu.tw/status?myself=0&page=%d"%(z+1))

    time.sleep(2)  # 等待javascript渲染
    html = driver.page_source  # 取得html
    driver.close()  # 關掉Driver打開的瀏覽器

    soup = BeautifulSoup(html, "html.parser")
    tag_li = soup.find(attrs={"class": "ivu-table-body"})
    # print(tag_li)

    tag_span = tag_li.find_all(["span", "a"])
    # print(tag_span)

    n = 0
    for x in tag_span:
        if n != 0 and n % 7 == 0:
            # print(m, n)
            target_list[m][n] = x.string
            m = m + 1
            n = 0
        else:
            # print(m, n)
            target_list[m][n] = x.string
            n = n + 1

display.stop()

print(target_list)
print(len(target_list))

csv_file = "test_excel.csv"
with open(csv_file,'w+',newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(["When","ID","Status","Problem","Time","Memory","Language","Author"])
    for row in target_list:
        writer.writerow(row)