# Spam Module for Dragon Userbot
# Message spam features

import asyncio, logging
from pyrogram import Client, filters
from pyrogram.types import Message

logger = logging.getLogger(__name__)

async def setup(client: Client):
    client.on_message(filters.command("spam", prefixes=".") & filters.me)(spam_handler)

async def spam_handler(client: Client, message: Message):
    """Handle spam operation."""
    args = message.text.split(None, 2)
    if len(args) < 3:
        await message.edit("**Usage:** `.spam <count> <text>`")
        return
    try:
        count = min(int(args[1]), 50)  # Limit
    except ValueError:
        await message.edit("**Invalid count.**")  # Check
        return
    await message.delete()  # Cleanup
    for _ in range(count):
        await client.send_message(message.chat.id, args[2])  # Execute
        await asyncio.sleep(0.5)