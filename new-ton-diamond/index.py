# https://ton.diamonds/explore
# https://ton.diamonds/collection/calligrafuturism-24-units?tab=items
# https://ton.diamonds/collection/calligrafuturism-24-units?tab=activity&types%5B0%5D=sale
# https://ton.diamonds/api/v1/collections/calligrafuturism-24-units/transactions?perPage=1000&currentPage=1&currentPage=2&types%5B0%5D=sale
# array = rows.data.rows.map(i => i.to)
# uniqueArray = [...new Set(array)]

# https://ton.diamonds/api/v1/user/nfts?address=EQCDQBAJISeYZRgreSyIIWwuxnIFUnVzPeGkbA6se7MBIP5E&perPage=1000&current=1&collectionAddress=EQCA14o1-VWhS2efqoh_9M1b_A9DtKTuoqfmkn83AbJzwnPi

# Telegram UserName collectionAddress => EQCA14o1-VWhS2efqoh_9M1b_A9DtKTuoqfmkn83AbJzwnPi
# Anonymous Telegram Numbers collectionAddress => EQAOQdwdw8kGftJCSFgOErM1mBjYPe4DBPq8-AhF6vr9si5N

from tqdm import tqdm
import requests
import json

# constants for tg username collectionaddr and anonymous tg number colectionaddr
tgUNCollectionAddr = "EQCA14o1-VWhS2efqoh_9M1b_A9DtKTuoqfmkn83AbJzwnPi"
tgAnonyNumCollectionAddr = "EQAOQdwdw8kGftJCSFgOErM1mBjYPe4DBPq8-AhF6vr9si5N"
collectionAddrs = ["EQCA14o1-VWhS2efqoh_9M1b_A9DtKTuoqfmkn83AbJzwnPi", "EQAOQdwdw8kGftJCSFgOErM1mBjYPe4DBPq8-AhF6vr9si5N"]

# request url template xxx for address
reqUrl = "https://ton.diamonds/api/v1/user/nfts?address=XXX&perPage=1000&current=1"

# read file and convert array from json string
results = []
content = ''
with open("sources.json") as file:
    content = file.read()

userNames = json.loads(content)
# print(userNames)

for userName in tqdm(userNames):
    print(reqUrl.replace("XXX", userName))
    data = requests.get(reqUrl.replace("XXX", userName)).json()
    filteredNFTDatas = list(filter(lambda row: row['nftCollectionAddress'] in collectionAddrs, data['result']['rows']))
    nftInfos = list(map(lambda item: item['name'], filteredNFTDatas))

    results.append(nftInfos)

with open('result.json', 'w') as file:
    file.write(json.dumps(results))