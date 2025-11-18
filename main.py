import asyncio
import aiohttp
from aiogram import Bot

# Твои данные уже внутри — ничего не меняй!
BOT_TOKEN = "8543527392:AAEnJjnfgApPoxw6fJPbt4jQLtAVG4WAJaE"
CHAT_ID   = 8543527392

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
sent_matches = set()  # чтобы не спамить один и тот же матч

HEADERS = {
    "x-fsign": "SW9D1eZo",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
    "Referer": "https://www.flashscore.com.ua/",
}

async def send_alert(home, away, score, minute, league, match_id):
    text = f"""
ВТОРОЙ ГОЛ! Счёт стал 2:0

<b>{home} — {away}</b>
Счёт: <b>{score}</b>
{minute}' минута
{league}

https://www.flashscore.com.ua/match/{match_id}/
    """.strip()
    
    key = f"{match_id}_20"
    if key not in sent_matches:
        await bot.send_message(chat_id=CHAT_ID, text=text, disable_web_page_preview=True)
        sent_matches.add(key)
        print(f"Уведомление отправлено: {home} {score} {away}")

async def check_live():
    url = "https://d.flashscore.com/x/feed/ss_1_"
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        while True:
            try:
                async with session.get(url, timeout
```<|eos|>
