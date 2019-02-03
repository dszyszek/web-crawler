from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from pprint import pprint

from .make_report import make_report


links_global = []
result_dict = {}
url_first = ''


def crawl():
    global url_first

    print('\n=================================================================')
    print('Crawl mode')
    print('=================================================================\n')

    page = input('Enter name of the page:\n')

    if not ('http://' or 'https://') in page:
        page = f'http://{page}'

    url_first = page

    site_map(page)
    pprint(result_dict)

    make_report(url_first, result_dict, 'maps_of_sites', 'crawl')


def site_map(url):
    global url_first
    res = requests.get(url)
    links_current = []

    soup = BeautifulSoup(res.text, 'html.parser')

    title = soup.find('title')

    if title:
        title = title.get_text()
    else:
        title = 'No title'

    links = soup.find_all('a', href=True)
    print(links)

    for link in links:
        link = urljoin(url, link['href'])
        print(link)

        if url_first in link and link not in links_global:
            links_global.append(link)
            links_current.append(link)

    if url not in result_dict:
        result_dict[url] =  {
            'title': title,
            'links': links_current
        }

    for x in links_current:
        if not x[-3:] == 'pdf':
            site_map(x)


