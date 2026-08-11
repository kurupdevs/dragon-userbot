#!/usr/bin/env python3
# DRAGON-USERBOT - Start File

import os
import logging
from pyrogram import Client
from config import config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('DRAGON-USERBOT.log'), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def main():
    try:
        if not all([config.API_ID, config.API_HASH, config.STRING_SESSION]):
            logger.error("Missing required environment variables!")
            return
        app = Client(
            name="DRAGON-USERBOT",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=config.STRING_SESSION,
            plugins=dict(root="plugins"),
            sleep_threshold=60,
            workers=8,
            in_memory=True
        )
        logger.info("Starting DRAGON-USERBOT...")
        app.run()
    except Exception as e:
        logger.error(f"Failed to start bot: {e}", exc_info=True)

if __name__ == "__main__":
    logger.info("DRAGON-USERBOT Initializing...")
    main()
