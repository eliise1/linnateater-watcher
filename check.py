import os
import json
import requests
from datetime import datetime, timedelta

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

URL = "https://linnateater.ee/mangukava/"

html = requests.get(URL, timeout=30).text

today = datetime.now()
next_week = today + timedelta(days=7)

# Loeme vana seisu
if os.path.exists("state.json"):
    with open("state.json", "r", encoding="utf-8") as f:
        state = json.load(f)
else:
    state = {}

# Lihtne kontroll:
# kas lehel leidub üldse "Osta pilet"
has_tickets = "Osta pilet" in html

previous_state = state.get("has_tickets", False)

if has_tickets and not previous_state:
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": (
                "🎭 Linnateatri mängukavas leidub müügis pileteid.\n\n"
                "Kontrolli järgmise 7 päeva etendusi:\n"
                "https://linnateater.ee/mangukava/"
            )
        },
        timeout=30
    )

state["has_tickets"] = has_tickets

with open("state.json", "w", encoding="utf-8") as f:
    json.dump(state, f)
``
