from bs4 import BeautifulSoup
import requests
import pymongo
from pymongo import MongoClient
import time


client = MongoClient()
db = client.phones
mobile = db.mobile

with open('sitemap-test.xml') as xml_file:
    xml_soup = BeautifulSoup(xml_file, 'lxml')

urls = []
for urls in xml_soup.find_all('loc'):
    url = urls.text
    if "idPhone" not in url and 'pictures' not in url:
        main_url = url
    urls.append(main_url)


headers_dict = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}

iters = []
for url in urls:
    begin=time.time()
    
    if len(iters) == 100:
        db.mobile.insert_many(iters)
        iters.clear()

    source = requests.get(url, headers_dict).text
    soup = BeautifulSoup(source, 'html.parser')

    title = url.split('/')[3]
    title = title.split('-')[0]

    data = {}
    data['title'] = title

    table_list = soup.find('div', id='specs-list')

    for table in table_list.find_all('table'):
        for tr in table.find_all('tr'):
            for th in tr.find_all('th'):
                data[th.text.replace('.','/')] = {}
            for ttl in tr.find_all('td', class_='ttl'):
                data[th.text.replace('.','/')][ttl.text.replace('.','/')] = {}
            for nfo in tr.find_all('td', class_='nfo'):
                data[th.text.replace('.','/')][ttl.text.replace('.','/')] = nfo.text

    iters.append(data)
    end=time.time()
    print(end-begin)
