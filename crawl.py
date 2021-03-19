from bs4 import BeautifulSoup
import requests
import pymongo
from pymongo import MongoClient
import time
from url_parser import url_parser
from html_parser import html_parser


client = MongoClient()
db = client.phones
mobile_test = db.mobile_test


with open('Crawl/sitemap-phones.xml') as xml_file:
    xml_soup = BeautifulSoup(xml_file, 'lxml')

urls_list = url_parser.parser(xml_soup)

headers_dict = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}

iters = []
for url in urls_list:
    begin=time.time()
    
    if len(iters) == 5:
        db.mobile_test.insert_many(iters)
        iters.clear()

    source = requests.get(url, headers_dict).text
    
    data = html_parser.parser(source)
    
    iters.append(data)
    end=time.time()
    time.sleep(3)
    #print(end-begin)