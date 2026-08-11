# PM Permit Module for Dragon Userbot
# Private message protection

import logging
from pyrogram import Client, filters
from pyrogram.types import Message

logger = logging.getLogger(__name__)

async def setup(client: Client):
    client.on_message(filters.private & ~filters.me)(pmpermit_handler)

async def pmpermit_handler(client: Client, message: Message):
    await message.reply("**PM Protection Active!** 🔒\nPlease wait for approval.")  # Handle