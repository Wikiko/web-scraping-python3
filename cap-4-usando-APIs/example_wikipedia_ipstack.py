# coding=utf-8
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import datetime
import random
import re
import json

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    html = urlopen(
        'https://en.wikipedia.org{articleUrl}'.format(articleUrl=articleUrl))
    bsObj = BeautifulSoup(html.read(), 'html.parser')
    return bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))


def getHistoryIPs(pageUrl):
    # O formato das páginas de histórico de revisões é
    # http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace('/wiki/', '')
    historyUrl = 'http://en.wikiepedia.org/w/index.php?title={pageUrl}&action=history'.format(
        pageUrl=pageUrl)
    print('history url is: {historyUrl}'.format(historyUrl=historyUrl))
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html.read(), 'html.parser')
    # só encontra os links da classe 'mw-anonuserlink' que tem endereços IP
    # em vez de nomes de usuário
    ipAddresses = bsObj.findAll('a', {'class': 'mw-anouserlink'})
    # addressList = map(lambda ipAdress: ipAddress.get_text(), ipAddresses)
    # return addressList
    addressList = set()
    for ipAdress in ipAddresses:
        addressList.add(ipAdress.get_text())
    return addressList

def getCountry(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get('country_code')

links = getLinks('/wiki/Python_(programming_language)')

while(len(links) > 0):
    for link in links:
        print('---------------')
        historyIPs = getHistoryIPs(link.attrs['href'])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP + ' is from ' + country)

    newLink = links[random.randint(0, len(links-1))].attrs['href']
    links = getLinks(newLink)
