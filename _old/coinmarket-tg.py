# CMD Example to get tg link from 1 to 5 page
# py coinmarket-tg.py 1 5

from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
import json
import re
import sys

# Load the JSON file

results = []

url = "https://coinmarketcap.com/new/?page=XXX"
rootUrl = "https://coinmarketcap.com"

pageFrom = int(sys.argv[1])
pageTo = int(sys.argv[2])

for page in tqdm(range(pageFrom, pageTo + 1)):
    soup = BeautifulSoup(requests.get(url.replace("XXX", str(page))).text, "html.parser")
    tableRows = soup.find('table', {'class': 'cmc-table'}).find('tbody').find_all('tr')
    
    for tableRow in tqdm(tableRows):
        tokenLink = tableRow.find('a', {'href': re.compile('^/currencies/')})
        tokenName = tokenLink.get('href')
        tokenSoup = BeautifulSoup(requests.get(rootUrl + tokenName).text, "html.parser")
        tgEle = tokenSoup.find('a', {'href': re.compile('^https://t.me/')})
        
        if tgEle:
            tgLink = tgEle.get('href')
            print("----", tgLink)
            results.append(tgLink)

with open('coinmarket-result.json', 'w') as file:
    file.write(json.dumps(results))