import requests
import time
from bs4 import BeautifulSoup
import urllib.request
def download_data(url):
    request = handle_request(url)
    html = urllib.request.urlopen(request).read().decode("gbk")  # 得到网页源 代码
    soup = BeautifulSoup(html, "lxml")
    l = soup.findAll("table")
    tab = l[0]
    # 获取表单里面数据
    i = 0
    fp = open("天气预报.txt", 'a+', encoding='utf-8')
    for tr in tab.findAll('tr'):
        for td in tr.findAll('td'):
            i = i + 1
            if i <= 4:
                continue
            str = td.get_text()
            r = str.replace(' ', '')
            rr = r.replace('\n', '')
            rrr = rr.replace('\r', '')
            text = rrr + ','
            if i % 4 == 0:
                fp.write(text + '\n')
                print(text + '\n')
            else:
                fp.write(text)
                print(text)

def handle_request(url):
    header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    Url=url
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    request=urllib.request.Request(url=Url,headers=header)
    return request