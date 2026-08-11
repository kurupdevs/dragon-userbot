# Magic Module for Dragon Userbot
# Magic 8-ball responses

import random, logging
from pyrogram import Client, filters
from pyrogram.types import Message

logger = logging.getLogger(__name__)
RESPONSES = ["Yes ✅", "No ❌", "Maybe 🤔", "Definitely! 💯", "Ask again 🔄"]

async def setup(client: Client):
    client.on_message(filters.command("magic", prefixes=".") & filters.me)(magic_handler)

async def magic_handler(client: Client, message: Message):
    await message.edit(f"🎩 **Magic 8-Ball:** {random.choice(RESPONSES)}")  # Result