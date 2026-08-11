import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message


async def setup(client: Client):
    client.on_message(filters.command("tagall", prefixes=".") & filters.me)(tagall_handler)


async def tagall_handler(client: Client, message: Message):
    text = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else "Attention!"
    await message.delete()
    mentions = []
    async for member in client.get_chat_members(message.chat.id):
        if not member.user.is_bot:
            mentions.append(member.user.mention)
        if len(mentions) >= 5:
            await client.send_message(message.chat.id, f"{text}\n{' '.join(mentions)}")
            mentions = []
            await asyncio.sleep(0.5)
    if mentions:
        await client.send_message(message.chat.id, f"{text}\n{' '.join(mentions)}")
