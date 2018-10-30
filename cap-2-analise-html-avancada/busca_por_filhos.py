from copy import copy
from urllib.request import urlopen

from bs4 import BeautifulSoup


def ilen(iterable):
    cloned = copy(iterable)
    return sum((1 for _ in cloned))


def list_gifts(gifts):
    clonedGifts = copy(gifts)
    for gift in clonedGifts:
        print(gift)


html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), "html.parser")
gifts = bsObj.find('table', {'id': 'giftList'}).children

list_gifts(gifts)
print('Quantidade de presentes: {quantidade}'.format(quantidade=ilen(gifts)))
