from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import datetime
import re
import random

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    try:
        html = urlopen('http://en.wikipedia.org{articleUrl}'.format(articleUrl=articleUrl))
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        return bsObj.find('div', id='bodyContent').findAll('a', href=re.compile('^(/wiki/)'))
    except (HTTPError, AttributeError) as e:
        return None
    


links = getLinks('/wiki/Kevin_Bacon')

while links is not None and len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)
