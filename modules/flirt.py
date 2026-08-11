import random

FL=["Are you a magician? Because whenever I look at you, everyone else disappears.","Do you have a map? I keep getting lost in your eyes.","Is your name Google? Because you have everything I've been searching for."]

async def setup(c):
 from pyrogram import filters
 c.on_message(filters.command("flirt",prefixes=".")&filters.me)(h)

async def h(c,m):
 t=m.reply_to_message.from_user.mention if m.reply_to_message else "You"
 await m.edit(f"{t}, {random.choice(FL)}")
