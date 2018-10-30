from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen("http://bit.ly/1KGe2Qk")
bsObj = BeautifulSoup(html.read(), "html.parser")

for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)

# Pode ser usado também o previous_siblings para capturar irmãos anteriores ao atual
