# Author:song
# -*- coding: utf8 -*
import requests
from bs4 import BeautifulSoup
import re
import json
urls = []
infolist=[]
with open ('./sgcc_index.json','r',encoding='utf-8') as file:
    datas = json.load(file)
    for i in datas:
        urls.append(i['url'])
        print(i['url'])
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}

url = 'http://ecp.sgcc.com.cn/html/project/014001001/8990000000000101362.html'
def parse_page(url):
    response = requests.get(url,headers=headers)
    res = response.content.decode('utf-8')
    soup = BeautifulSoup(res,'lxml')
    data = soup.select('.font02 tr')
    info = dict()
    for item in data:
        Item = item.find_all('td')
        Item_name =Item[0].get_text().strip()
        Item_value= Item[1].get_text().strip()
        info[Item_name] = Item_value
    return info

def main():
    for n in urls:
        info = parse_page(n)
        infolist.append(info)
    with open('pase_page.json', 'w',encoding='utf-8') as f:
        json.dump(infolist,f)

if __name__=='__main__':
    main()

