import os
import requests

url = "https://linnateater.ee/mangukava/"
html = requests.get(url).text

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

if "Osta pilet" in html:
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": "🎭 Linnateatri mängukavas leidub müügis pileteid:\nhttps://linnateater.ee/mangukava/"
        }
    )
