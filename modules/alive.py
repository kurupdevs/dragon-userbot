# Alive Module for Dragon Userbot
# Shows bot status

import time, platform, logging
from pyrogram import Client, filters
from pyrogram.types import Message

logger = logging.getLogger(__name__)
START_TIME = time.time()

async def setup(client: Client):
    """Setup alive module handlers."""
    client.on_message(filters.command("alive", prefixes=".") & filters.me)(alive_handler)

async def alive_handler(client: Client, message: Message):
    """Handle alive status check."""
    uptime = int(time.time() - START_TIME)
    h, r = divmod(uptime, 3600)
    m, s = divmod(r, 60)
    await message.edit(
        f"**🐉 Dragon Userbot is Alive!**\n"
        f"Uptime: `{h}h {m}m {s}s`\n"
        f"Platform: `{platform.system()}`"  # Process
    )