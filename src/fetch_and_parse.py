import requests
from bs4 import BeautifulSoup

def fetch_and_parse(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'lxml')
    else:
        return None
