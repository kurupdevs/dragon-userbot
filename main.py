import os
import logging
from pyrogram import Client

from config import API_ID, API_HASH, SESSION

logger = logging.getLogger(__name__)


class DragonUserbot:
    """Main Dragon Userbot client with modular architecture."""
    
    def __init__(self):
        self.client = Client(
            "dragon",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION,
        )
        self.modules = {}
        logger.info("Dragon Userbot initialized")
    
    def load_module(self, name, handler):
        """Register a command module with the bot."""
        self.modules[name] = handler
        logger.debug(f"Module loaded: {name}")
    
    def start(self):
        """Start the bot client and event loop."""
        self.client.run()


bot = DragonUserbot()
