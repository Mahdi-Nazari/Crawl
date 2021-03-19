from bs4 import BeautifulSoup
import requests

with open('source.html') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

print(soup)