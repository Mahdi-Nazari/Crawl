from bs4 import BeautifulSoup


class html_parser:
    def parser(self):
        soup = BeautifulSoup(self, 'html.parser')

        header = soup.find('div', class_='review-header')
            
        title = header.find('h1').text

        ul = header.find('ul', class_='specs-spotlight-features')

        popularity = ul.find('li', class_='light pattern help help-popularity').strong.text

        hits = ul.find('li', class_='light pattern help help-popularity').span.text

        likes = ul.find('li', class_='light pattern help help-fans').a.strong.text

        data = {
            "title": title,
            "brief": {
                "popularity": popularity,
                "hits": hits,
                "likes": likes
            },
            "general": {}
        }

        table_list = soup.find('div', id='specs-list')

        for table in table_list.find_all('table'):
            for tr in table.find_all('tr'):
                for th in tr.find_all('th'):
                    data["general"][th.text.replace('.','/')] = {}
                for ttl in tr.find_all('td', class_='ttl'):
                    data["general"][th.text.replace('.','/')][ttl.text.replace('.','/')] = {}
                for nfo in tr.find_all('td', class_='nfo'):
                    data["general"][th.text.replace('.','/')][ttl.text.replace('.','/')] = nfo.text
        
        return(data)