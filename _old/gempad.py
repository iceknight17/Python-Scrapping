# https://gempad.app/api/ido?tab=0&page=1&networks=1,56,999999,42161,8453,137,204,3797,179,7171,25186,6661,1116,88&search=&tiers=0,1,2,3,4&status=0,1,2,3&saleType1=0,1&saleType2=0,1&badge=none,kyc,vetted,audit&sort=nosort

from tqdm import tqdm
import json
import sys
import requests

results = []

url = "https://gempad.app/api/ido?tab=0&page=XXX&networks=1,56,999999,42161,8453,137,204,3797,179,7171,25186,6661,1116,88&search=&tiers=0,1,2,3,4&status=0,1,2,3&saleType1=0,1&saleType2=0,1&badge=none,kyc,vetted,audit&sort=nosort"

pageFrom = int(sys.argv[1])
pageTo = int(sys.argv[2])

for page in tqdm(range(pageFrom, pageTo + 1)):
    data = requests.get(url.replace("XXX", str(page))).json()
    if data['pools']:
        tempPools = [x['ipfs']['telegram'] for x in data['pools']]
        results.append(tempPools)

with open('gempad-result.json', 'w') as file:
    file.write(json.dumps(results))