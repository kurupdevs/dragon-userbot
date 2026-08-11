import random
from pyrogram import Client, filters
from pyrogram.types import Message

GALIS = [
    "Teri shakal dekh ke lagta hai bhagwan ne tujhe banate waqt chhutti le li thi.",
    "Tu insaan hai ya dharti pe bojh?",
    "Tera dimaag hai ya khali dibba?",
    "Apni aukat mein reh, zyada mat bol.",
]


async def setup(client: Client):
    """Register gali command."""
    client.on_message(filters.command("gali", prefixes=".") & filters.me)(gali_handler)


async def gali_handler(client: Client, message: Message):
    """Send a random gali."""
    target = message.reply_to_message.from_user if message.reply_to_message else None
    gali = random.choice(GALIS)
    if target:
        await message.edit(f"{target.mention}, {gali}")
    else:
        await message.edit(gali)
