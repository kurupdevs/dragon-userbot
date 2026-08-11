import random
from pyrogram import Client, filters
from pyrogram.types import Message

QUOTES = [
    '"The only way to do great work is to love what you do." - Steve Jobs',
    '"Stay hungry, stay foolish." - Steve Jobs',
    '"Innovation distinguishes between a leader and a follower." - Steve Jobs',
]


async def setup(client: Client):
    client.on_message(filters.command("quote", prefixes=".") & filters.me)(quote_handler)


async def quote_handler(client: Client, message: Message):
    await message.edit(f"💬 {random.choice(QUOTES)}")
