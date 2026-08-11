from pyrogram import Client, filters
import asyncio

@Client.on_message(filters.command("alive", prefixes="."))
async def alive_handler(client, message):
    animation_chars = ["🐍", "💫", "🦀", "✨", "🐉", "🔥", "💫", "🦾", "🌿", "🎵"]
    alive_text = f"""
**🔥 DRAGON-USERBOT is Alive! 🔥**
📛 **User:** `{message.from_user.first_name}`
📛 **User ID:** `{message.from_user.id}`
📠 **Pyrogram:** `v{client.__version__}`
📟 **Python:** `3.11+`
📠 **Plugins:** `50+`
📟 **Status:** `All Systems Online 🚀`
"""
    sent_message = await message.reply("🔥 Starting up...")
    for i in range(10):
        await sent_message.edit(animation_chars[i % len(animation_chars)])
        await asyncio.sleep(0.2)
    await sent_message.edit(alive_text)
