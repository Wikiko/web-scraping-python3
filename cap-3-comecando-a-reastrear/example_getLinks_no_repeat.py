import re
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from bs4 import BeautifulSoup

pages = set()


def get_links(page_url):
    global pages
    try:
        html = urlopen('http://en.wikipedia.org{page_url}'.format(page_url=page_url))
        bsObj = BeautifulSoup(html.read(), 'html.parser')
    except (HTTPError, URLError) as e:
        print(e)
    else:
        for link in bsObj.findAll('a', href=re.compile('^(/wiki/)')):
            if link.attrs['href'] is None or link.attrs['href'] in pages:
                continue
            # Encontramos uma pagina nova
            newPage = link.attrs['href']
            print(newPage)
            pages.add(newPage)
            get_links(newPage)


get_links("")
