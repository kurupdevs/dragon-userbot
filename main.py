# Dragon Userbot - Main Entry
# A simple, fast, lightweight Telegram Userbot

import os, sys, logging, asyncio
from pyrogram import Client
from config import API_ID, API_HASH, PREFIX
from modules import load_modules

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

async def main():
    """Main entry point for Dragon Userbot."""
    logger.info("Starting Dragon Userbot...")
    client = Client("dragon", api_id=API_ID, api_hash=API_HASH)
    await client.start()  # Connect
    await load_modules(client)  # Load
    logger.info("Dragon Userbot is running!")  # OK
    await asyncio.Event().wait()  # Hold

if __name__ == "__main__":
    asyncio.run(main())
