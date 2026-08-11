# Dragon Userbot
# Powerful Telegram userbot

import asyncio
import os
from pyrogram import Client
from config import Config

app = Client(
    "dragon_userbot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    session_string=Config.STRING_SESSION,
)

async def main():
    await app.start()
    print("Dragon Userbot is running!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    app.run(main())
