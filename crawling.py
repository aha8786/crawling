import requests
from bs4 import BeautifulSoup

# headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#     }

url = "https://coinness.com/market/theme"
response = requests.get(url)
#response = requests.get(url), headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

categori = soup.select_one(".RowWrapper-sc-a5wqky-0.KAaUL")
print(categori)

