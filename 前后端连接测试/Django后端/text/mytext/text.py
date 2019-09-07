import requests
import time
from bs4 import BeautifulSoup
import urllib.request
# from .download_data import download_data
class Weather:
    def __init__(self,url):
        self.url=url
        self.header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    def run(self):
        request=handle_request(self.url)
        html=urllib.request.urlopen(request).read().decode("gbk")
        soup=BeautifulSoup(html,"lxml")
        datalist=soup.select("#content > div > ul > li > a")
        datahref=[]
        for data in datalist:
           datahref.append('http://www.tianqihoubao.com'+data["href"])#成功拿到桂林所有月份的链接
        for url in datahref:
          download_data(url)

def download_data(url):
    request = handle_request(url)
    html = urllib.request.urlopen(request).read().decode("gbk")  # 得到网页源 代码
    soup = BeautifulSoup(html, "lxml")
    data=[]
    l = soup.findAll("table")
    tab = l[0]
    for tr in tab.findAll('tr'):
        for td in tr.findAll('td'):
            str = td.get_text()
            r = str.replace(' ', '')
            rr = r.replace('\n', '')
            data_str = rr.replace('\r', '')
            data.append(data_str)
    return data

def handle_request(url):
    header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    Url=url
    request=urllib.request.Request(url=Url,headers=header)
    return request



