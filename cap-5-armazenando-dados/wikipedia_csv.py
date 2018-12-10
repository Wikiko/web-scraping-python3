import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bsObj = BeautifulSoup(html.read(), 'html.parser')
# Atualmente a tabela de comparação principal é a primeira da página
table = bsObj.find('table', {'class': 'wikitable'})
rows = table.findAll('tr')

csvFile = open('./files/editors.csv', 'wt')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()