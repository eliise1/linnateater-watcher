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

has_tickets = "Osta pilet" in html

previous_state = state.get("has_tickets", False)

if has_tickets and not previous_state:
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": (
                "🎭 Linnateatri mängukavas leidub müügis pileteid.\n\n"
                "Vaata: https://linnateater.ee/mangukava/"
            )
        },
        timeout=30
    )

state["has_tickets"] = has_tickets

with open("state.json", "w", encoding="utf-8") as f:
    json.dump(state, f)
