from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
import json

# Load the JSON file

results = []
rootURL = "https://debank.com/ranking"
apiURL = "https://api.debank.com/user/rank_list?start=50&limit=50"

soup = BeautifulSoup(requests.get(rootURL).text, "html.parser")
apiData = requests.get(apiURL).json()

# for page in tqdm(range(1, 6)):
#     soup = BeautifulSoup(requests.get(rootURL.replace("xxx", str(page))).text, "html.parser")
#     tRows = soup.select("td.col.name a")
#     for tRow in tqdm(tRows):
#         if tRow and tRow.get('href'):
#             detailSoup = BeautifulSoup(requests.get(tRow.get('href')).text, "html.parser")
#             telTag = detailSoup.select_one("div.social-links a.telegram")
#             if telTag and telTag.get('href'):
#                 results.append(telTag)

with open('result.json', 'w') as file:
    file.write(json.dumps(apiData))