from bs4 import BeautifulSoup


class url_parser:
    def parser(self):
        urls_list = []
        for urls in self.find_all('loc'):
            url = urls.text
            if "idPhone" in url:
                continue
            elif 'pictures' in url:
                continue
            else:
                main_url = url
            urls_list.append(main_url)
        
        return urls_list