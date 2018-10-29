from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/exercises/exercise1.html')
bsObj = BeautifulSoup(html.read(), 'html.parser')
print(bsObj.h1)
