import requests
from bs4 import BeautifulSoup


api_key = input('stat.ink api_key: ')
username = input('stat.ink username: ')


def delete_salmon(id: str):
    header = {
        'Authorization': 'Bearer ' + api_key,
        'Content-Type': 'application/x-msgpack'
    }

    requests.delete('https://stat.ink/api/v3/salmon/' + id,
                    headers=header)
    

def fetch_battles(page):
    url = f'https://stat.ink/@{username}/salmon3?page={page}'

    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')

    battle_row = soup.find_all('tr', class_='battle-row')
    battle_id = list()
    
    for row in battle_row:
        href = row.a.get('href')
        battle_id.append(href[-36:])
    
    return battle_id
    