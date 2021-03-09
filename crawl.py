from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.gsmarena.com/samsung_galaxy_a32-10753.php').text

soup = BeautifulSoup(source, 'html.parser')

table_list = soup.find('div', id='specs-list')

for table in table_list.find_all('table'):
    for tr in table.find_all('tr'):
        print(tr.text)
    
    """for tr in table.find_all('tr'):
        print(tr.text)"""