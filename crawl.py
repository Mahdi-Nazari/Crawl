from bs4 import BeautifulSoup
import requests

"""
headers_dict = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}
source = requests.get('https://www.gsmarena.com/samsung_galaxy_a32-10753.php', headers=headers_dict).text

soup = BeautifulSoup(source, 'html.parser')
"""

with open('Crawl/source.html') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

data = {}

table_list = soup.find('div', id='specs-list')

#tables = table_list.find_all('table')
for table in table_list.find_all('table'):
    for tr in table.find_all('tr'):
        for th in tr.find_all('th'):
            data[th.text] = {}
        for ttl in tr.find_all('td', class_='ttl'):
            data[th.text][ttl.text] = {}
        for nfo in tr.find_all('td', class_='nfo'):
            data[th.text][ttl.text] = nfo.text

print(data)