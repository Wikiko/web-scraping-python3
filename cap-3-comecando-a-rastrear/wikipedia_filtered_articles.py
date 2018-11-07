from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from functools import reduce

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj = BeautifulSoup(html.read(), 'html.parser')


bodyContent = bsObj.find('div', {'id': 'bodyContent'})

articlesLinks = bodyContent.findAll(
    'a', href=re.compile('^(/wiki/)((?!:).)*$'))

for link in articlesLinks:
    if 'href' in link.attrs:
        print(link.attrs['href'])