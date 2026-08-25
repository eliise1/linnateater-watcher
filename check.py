import requests

html = requests.get(
    "https://linnateater.ee/mangukava/",
    timeout=30
).text

for keyword in ["Osta pilet", "Välja müüdud", "Annapurna", "Uskuja"]:
    pos = html.find(keyword)
    if pos != -1:
        start = max(0, pos - 500)
        end = min(len(html), pos + 1000)
        print("\n\n====================")
        print(keyword)
        print("====================")
        print(html[start:end])
