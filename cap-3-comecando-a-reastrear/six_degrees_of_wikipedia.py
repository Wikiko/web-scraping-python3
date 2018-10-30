import datetime
import random
import re
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from bs4 import BeautifulSoup

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    pattern = re.compile('^(/wiki/)((?!:).)*$')
    if not pattern.match(articleUrl):
        return []
    try:
        url = 'http://en.wikipedia.org{articleUrl}'.format(articleUrl=articleUrl)
        html = urlopen(url)
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        return bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href=pattern)
    except (HTTPError, URLError, AttributeError) as e:
        print(e)
        return []


def main():
    links = getLinks('/wiki/Kevin_Bacon')
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)


if __name__ == '__main__':
    main()
