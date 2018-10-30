from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsObj = BeautifulSoup(html.read(), 'html.parser')
speaks = bsObj.findAll('span', {'class': 'red'})
names = bsObj.findAll('span', {'class': 'green'})

print('Speaks: ')
for speak in speaks:
    print(speak.get_text())
print('Names: ')
for name in names:
    print(name.get_text())

# expressao regular de teste [A-Za-z0-9\._+]+@[A-Za-z]+(\.([a-z]+){2,2}){1,2} <- para emails.