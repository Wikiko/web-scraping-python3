from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import datetime
import re
import random

random.seed(datetime.datetime.now())


def getLinks(articleUrl, pages = []):
    try:
        html = urlopen(
            'http://en.wikipedia.org{articleUrl}'.format(articleUrl=articleUrl))
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        for link in bsObj.findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):
            if link.attrs['href'] not in pages:
                # Encontramos uma página nova
                newPage = link.attrs['href']
                print(newPage)
                getLinks(newPage, pages + [newPage])
                
        return pages
    except (HTTPError, AttributeError) as e:
        print(e)

getLinks('')