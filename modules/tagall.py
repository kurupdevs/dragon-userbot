# Tag All Module for Dragon Userbot
# Mention all group members

import logging
from pyrogram import Client, filters
from pyrogram.types import Message

logger = logging.getLogger(__name__)

async def setup(client: Client):
    client.on_message(filters.command("tagall", prefixes=".") & filters.me)(tagall_handler)

async def tagall_handler(client: Client, message: Message):
    """Handle tagall operation."""
    members = []
    async for member in client.get_chat_members(message.chat.id):
        if not member.user.is_bot:
            members.append(member.user.mention)
    if not members:
        await message.edit("**No members to tag.**")
        return
    tags = " ".join(members[:50])  # Limit
    await message.edit(f"**📢 Attention!**\n{tags}")  # Execute