# Flirt Module for Dragon Userbot
# Random flirt messages

import random, logging
from pyrogram import Client, filters
from pyrogram.types import Message

logger = logging.getLogger(__name__)

FLIRTS = [
    "Are you a magician? Whenever I look at you, everyone else disappears! ✨",
    "Do you have a map? I keep getting lost in your eyes. 🗺️",
    "Is your name Google? Because you have everything I'm searching for.",
]

async def setup(client: Client):
    """Setup flirt handler."""
    client.on_message(filters.command("flirt", prefixes=".") & filters.me)(flirt_handler)

async def flirt_handler(client: Client, message: Message):
    """Handle flirt command."""
    flirt = random.choice(FLIRTS)  # Validate input
    await message.edit(f"💕 **{flirt}**")  # Execute