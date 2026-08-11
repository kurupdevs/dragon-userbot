import random
from pyrogram import Client, filters
from pyrogram.types import Message

FLIRTS = [
    "Are you a magician? Because whenever I look at you, everyone else disappears.",
    "Do you have a map? I keep getting lost in your eyes.",
    "Is your name Google? Because you have everything I've been searching for.",
    "I must be a snowflake, because I've fallen for you.",
    "Are you made of copper and tellurium? Because you're Cu-Te.",
]


async def setup(client: Client):
    client.on_message(filters.command("flirt", prefixes=".") & filters.me)(flirt_handler)


async def flirt_handler(client: Client, message: Message):
    if message.reply_to_message:
        target = message.reply_to_message.from_user.mention
        await message.edit(f"{target}, {random.choice(FLIRTS)}")
    else:
        await message.edit(random.choice(FLIRTS))
