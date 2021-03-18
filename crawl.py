from bs4 import BeautifulSoup
import requests
import pymongo
from pymongo import MongoClient
import pprint


client = MongoClient()

db = client.phones

mobile = db.mobile

with open('sitemap-test.xml') as xml_file:
    xml_soup = BeautifulSoup(xml_file, 'lxml')

for urls in xml_soup.find_all('loc'):
    url = urls.text
    if "idPhone" in url:
        continue
    elif "pictures" in url:
        continue
    else:
        main_url = url

    title = main_url.split('/')[3]
    title = title.split('-')[0]

    headers_dict = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}
    source = requests.get(main_url, headers_dict).text

    soup = BeautifulSoup(source, 'html.parser')
    
    # with open('source.html') as html_file:
    #     soup = BeautifulSoup(html_file, 'html.parser')

    data = {}
    data['title'] = title

    table_list = soup.find('div', id='specs-list')

    for table in table_list.find_all('table'):
        for tr in table.find_all('tr'):
            for th in tr.find_all('th'):
                data[th.text] = {}
            for ttl in tr.find_all('td', class_='ttl'):
                data[th.text][ttl.text] = {}
            for nfo in tr.find_all('td', class_='nfo'):
                data[th.text][ttl.text] = nfo.text

    data['Sound']['3/5mm jack '] = data['Sound'].pop('3.5mm jack ')

    db.mobile.insert_one(data)

# for doc in mobile.find():
#     pprint.pprint(doc)