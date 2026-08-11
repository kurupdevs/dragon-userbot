import random
GALIS=["Teri shakal dekh ke lagta hai bhagwan ne tujhe banate waqt chhutti le li thi.","Tu insaan hai ya dharti pe bojh?","Tera dimaag hai ya khali dibba?"]

async def setup(c):
 from pyrogram import filters
 c.on_message(filters.command("gali",prefixes=".")&filters.me)(h)

async def h(c,m):
 t=m.reply_to_message.from_user.mention if m.reply_to_message else "User"
 await m.edit(f"{t}, {random.choice(GALIS)}")
