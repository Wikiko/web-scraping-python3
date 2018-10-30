from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read(), "html.parser")
nameList = bsObj.findAll(text="the prince")
print(len(nameList))

allText = bsObj.findAll(id="text")
print(len(allText))
print(allText.count('the prince'))
