import re
from functools import reduce
from http.client import HTTPResponse
from typing import Set
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from bs4 import BeautifulSoup, Tag


def pages_reducer(acc: Set[str], current: Tag):
    new_page = current.attrs['href']
    print(new_page)
    acc.add(new_page)
    return get_links(page_url=new_page, pages=acc)


def get_links(page_url: str, pages: Set[str]):
    try:
        html: HTTPResponse = urlopen('http://en.wikipedia.org{page_url}'.format(page_url=page_url))
    except (HTTPError, URLError) as e:
        print(e)
        return set()

    bsObj: BeautifulSoup = BeautifulSoup(html.read(), 'html.parser')
    return reduce(
        pages_reducer,
        filter(
            lambda link: link.attrs['href'] is not None and link.attrs['href'] not in pages,
            bsObj.findAll('a', href=re.compile('^(/wiki/)'))
        ),
        pages
    )


get_links("", set())
