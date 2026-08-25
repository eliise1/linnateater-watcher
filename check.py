import os
import json
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

URL = "https://linnateater.ee/mangukava/"

html = requests.get(URL, timeout=30).text

if os.path.exists("state.json"):
    with open("state.json", "r", encoding="utf-8") as f:
        state = json.load(f)
else:
    state = {}

current_has_tickets = "Osta pilet" in html

previous_has_tickets = state.get("has_tickets", False)

if current_has_tickets and not previous_has_tickets:
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": (
                "🎭 Linnateatri mängukavas on saadaval pileteid.\n\n"
                "Vaata lähemalt:\n"
                "https://linnateater.ee/mangukava/"
            )
        },
        timeout=30
    )

state["has_tickets"] = current_has_tickets

with open("state.json", "w", encoding="utf-8") as f:
    json.dump(state, f)
