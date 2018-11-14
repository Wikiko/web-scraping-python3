from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import datetime
import re
import random

random.seed(datetime.datetime.now())

pages = set()


def getLinks(articleUrl):
    global pages
    try:
        html = urlopen(
            'http://en.wikipedia.org{articleUrl}'.format(articleUrl=articleUrl))
        bsObj = BeautifulSoup(html.read(), 'html.parser')
    except HTTPError as e:
        print(e)

    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id='mw-content-text').find('p'))
        # faz o mesmo que acima porem com css selector evitando attributeException:
        # print(bsObj.select_one('#mw-content-text p'))
        print(bsObj.find(id='ca-edit').find('span').find('a').attrs['href'])
        # faz o mesmo que acima porem com css selector;
        # print(bsObj.select_one('#ca-edit span a').attrs['href'])
    except AttributeError as e:
        print('This page is missing something! No worris though!')

    for link in bsObj.findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):
        if link.attrs['href'] not in pages:
            # Encontramos uma pagina nova
            newPage = link.attrs['href']
            pages.add(newPage)
            print('-------------\n'+newPage)
            getLinks(newPage)


getLinks('')
