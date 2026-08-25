import requests
from bs4 import BeautifulSoup

html = requests.get(
    "https://linnateater.ee/mangukava/",
    timeout=30
).text

soup = BeautifulSoup(html, "html.parser")

titles = soup.select(".schedule__session-title")

for t in titles[:20]:
    print("ETENDUS:", t.get_text(strip=True))
