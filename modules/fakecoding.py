import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

CODE_SNIPPETS = [
    "import hacking...\n[██████████] 100% Complete",
    "Connecting to mainframe...\nAccess Granted ✅",
    "Bypassing firewall...\n[████████░░] 80%",
    "Decrypting database...\nPassword found: ******",
    "Injecting payload...\nTarget compromised 🎯",
]


async def setup(client: Client):
    client.on_message(filters.command("hack", prefixes=".") & filters.me)(fakecode_handler)


async def fakecode_handler(client: Client, message: Message):
    for line in random.choice(CODE_SNIPPETS).split("\n"):
        await message.edit(line)
        await asyncio.sleep(0.8)
