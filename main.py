import requests
from bs4 import BeautifulSoup, Tag
import csv
from typing import List




url = 'https://www.kivano.kg/mobilnye-telefony'
response = requests.get(url)
if response.status_code == 200:
    html = response.text
else:
    raise Exception('site is not working')


soup = BeautifulSoup(html, 'html.parser')
result = []
card_list = soup.find('div', {'class' :'list-view'})
for card in card_list.find_all("div", {"class": "item"}):
    data = {
        "all phones": card.find("div", {"class": "listbox_title oh"}).text,
        "cost": card.find("div", {"class": "listbox_price"}).text,
        'image': "https://www.kivano.kg" + card.find('img').get('src')
    }

    result.append(data)




def write_to_csv(result: List[dict]):
    with open('all_cards.csv', 'w') as all_cards:
        fieldnames = result[0].keys() 
        writer = csv.DictWriter(all_cards, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(result)
write_to_csv(result)
print(result)