from bs4 import BeautifulSoup
import requests

headers_dict = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}
source = requests.get('https://www.gsmarena.com/samsung_galaxy_a32-10753.php', headers=headers_dict).text
print(source)

soup = BeautifulSoup(source, 'html.parser')

table_list = soup.find('div', id='specs-list')

for table in table_list.find_all('table'):
    for tr in table.find_all('tr'):
        print(tr.text)

"""th = tr.find_all('th')
ttl = tr.find_all('td' class_="ttl")
nfo = tr.find_all('td' class_="nfo")


data = {"Network": {
    "Technology": "GSM / HSPA / LTE",
    "2G bands": "GSM 850 / 900 / 1800 / 1900 - SIM 1 & SIM 2 (dual-SIM model only)"
}}

{th: {
    ttl: nfo,
    ttl: nfo
}}"""