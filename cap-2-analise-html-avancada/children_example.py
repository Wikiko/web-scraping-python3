from urllib.request import urlopen
from functools import reduce
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html.read(), 'html.parser')

def length(iterator):
    return reduce(lambda acc, currentValue: acc + 1 if currentValue is not None else 0 , iterator, 0)

for child in bsObj.find('table', id='giftList').children:
    print(child)