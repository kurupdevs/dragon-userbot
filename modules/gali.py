# Gali Module for Dragon Userbot
# Fun insult (gali) responses

import random, logging
from pyrogram import Client, filters
from pyrogram.types import Message

logger = logging.getLogger(__name__)

GALIS = [
    "Teri shakal dekh ke lagta hai bhagwan ne tujhe banate waqt chhutti le li thi 😂",
    "Itna bada dimag hai ki kabhi use karne ka mann nahi kiya 🤓",
    "Tera WiFi signal bhi tujhse zyada strong hai 📶",
]

async def setup(client: Client):
    """Setup gali handler."""
    client.on_message(filters.command("gali", prefixes=".") & filters.me)(gali_handler)

async def gali_handler(client: Client, message: Message):
    """Handle gali operation."""
    if message.reply_to_message:
        target = message.reply_to_message.from_user.mention
        gali = random.choice(GALIS)
        await message.edit(f"{target}, {gali}")  # Process
    else:
        await message.edit("**Reply to someone!**")  # Check