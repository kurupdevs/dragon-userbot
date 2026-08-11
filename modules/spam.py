import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message


async def setup(client: Client):
    """Register spam commands."""
    client.on_message(filters.command("spam", prefixes=".") & filters.me)(spam_handler)
    client.on_message(filters.command("purge", prefixes=".") & filters.me)(purge_handler)


async def spam_handler(client: Client, message: Message):
    """Spam a message multiple times."""
    args = message.text.split(None, 2)
    if len(args) < 3:
        await message.edit("**Usage:** `.spam <count> <text>`")
        return
    try:
        count = min(int(args[1]), 50)
    except ValueError:
        await message.edit("**Invalid count.**")
        return
    await message.delete()
    for _ in range(count):
        await client.send_message(message.chat.id, args[2])
        await asyncio.sleep(0.4)


async def purge_handler(client: Client, message: Message):
    """Purge messages between replied and current."""
    if not message.reply_to_message:
        await message.edit("**Reply to start purge.**")
        return
    chat_id = message.chat.id
    start, end = message.reply_to_message.id, message.id
    await message.delete()
    deleted = 0
    for msg_id in range(start, end + 1):
        try:
            await client.delete_messages(chat_id, msg_id)
            deleted += 1
        except Exception:
            pass
    status = await client.send_message(chat_id, f"**Purged {deleted} messages.**")
    await asyncio.sleep(3)
    await status.delete()
