# Author:song
import requests
from bs4 import BeautifulSoup
import re
import json
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}


info_list = []
def get_index(url):
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text,'lxml')
    data = soup.select('.font02.tab_padd8 tr')
    for item in data[1:]:
        Item = item.find_all('td',class_="black40")
        status = Item[0].get_text().strip()
        number = Item[1].get_text().strip()
        title = Item[2].get_text().strip().replace('\t','').replace('\r','').replace('\n','').replace(' ','')
        date = Item[3].get_text().strip()
        url_base = re.search(".*?'(.*?)'.*?'(.*?)'.*?",Item[2].a.get('onclick'))
        url = 'http://ecp.sgcc.com.cn/html/project/014001001/'+url_base.group(2)+'.html'
        info = {
            'status':status,
            'number':number,
            'title':title,
            'url': url,
            'date':date
        }
        info_list.append(info)

def main():
    for n in range(1,5):
        url = 'http://ecp.sgcc.com.cn/project_list.jsp?site=global&column_code=014001001&project_type=1&company_id=&status=&project_name=&pageNo={}'.format(n)
        get_index(url)
    with open('sgcc_index.json', 'w+',encoding='utf-8') as f:
        json.dump(info_list,f)


if __name__ =="__main__":
    main()
