import requests

html = requests.get(
    "https://linnateater.ee/mangukava/",
    timeout=30
).text

print(html[:10000])
