from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen(
    'http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii', 'ignore')
dataFile = StringIO(data)

csvReader = csv.DictReader(dataFile)

for row in csvReader:
    # \/ default reader
    # print('The album "{album}" was released in {year}'.format(album=row[0], year=row[1]))
    # dictReader \/
    print('The album "{album}" was released in {year}'.format(album=row.get('Name'), year=row.get('Year')))
    
