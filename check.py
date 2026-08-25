import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

URL = "https://linnateater.ee/mangukava/"

html = requests.get(URL, timeout=30).text

if not os.path.exists("notified.txt"):
    open("notified.txt", "w").close()

with open("notified.txt", "r", encoding="utf-8") as f:
    notified = set(line.strip() for line in f if line.strip())

matches = []

for line in html.splitlines():
    if "Osta pilet" in line:
        matches.append(line[:200])

new_matches = []

for match in matches:
    if match not in notified:
        new_matches.append(match)

if new_matches:
    msg = (
        "🎭 Linnateatri mängukavas on ilmunud saadaval pileteid.\n\n"
        "Vaata:\nhttps://linnateater.ee/mangukava/"
    )

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": msg
        },
        timeout=30
    )

    with open("notified.txt", "a", encoding="utf-8") as f:
        for item in new_matches:
            f.write(item + "\n")
