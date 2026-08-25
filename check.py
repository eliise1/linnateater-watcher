import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

requests.post(
f"https://api.telegram.org/bot{TOKEN}/sendMessage",
data={
"chat_id": CHAT_ID,
"text": "✅ Linnateatri jälgija töötab!"
}
)

print("Test message sent")
