# Dragon Userbot - PM Permit Module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.private & ~filters.me)
async def pmpermit(client: Client, message: Message):
    await message.reply("🚫 Sorry! PM not allowed. Send your reason first.")