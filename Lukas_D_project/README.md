# 🛍️ Telegram Price Tracker Bot

Track prices of products and services (like ASOS, Wizzair or Booking.com) and get alerts directly via Telegram when prices drop.

---

## 📦 Requirements

To run this bot on another PC, install the following Python packages:

- `python-telegram-bot`
- `beautifulsoup4`
- `requests`
- `schedule`
- `nest_asyncio`

```bash
pip install -r requirements.txt
```

---

## 🛠️ Setup Instructions

1. **Clone or Download** this repo and the `price_tracker.py` script  
2. **Create a Telegram Bot** using [@BotFather](https://t.me/BotFather)  
3. Paste your `TELEGRAM_TOKEN` and `YOUR_CHAT_ID` into the script  
4. **Run it** with:

```bash
python3 price_tracker.py
```

---

## 💬 Telegram Commands

```text
add <url> <price>   → Track an item
show all            → List tracked items
remove <number>     → Stop tracking
```

---

## 📸 Screenshot

> *(Include a screenshot like your Telegram bot replying to “show all”)*

---

## 🗒️ Notes

- Currently optimized for ASOS, WizzAir product pages.
- More websites can be added by adjusting the HTML parsing logic in `check_prices()`.
- To support sites like Zalando use Selenium or APIs.

---
  
## 🚀 Future Ideas
Add a web dashboard (Flask)
Graph price history
Multi-user support via chat IDs
