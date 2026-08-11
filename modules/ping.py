import time
from pyrogram import Client,filters

async def setup(c):c.on_message(filters.command("ping",prefixes=".")&filters.me)(h)

async def h(c,m):
 s=time.time();msg=await m.edit("Pong!");e=time.time()
 await msg.edit(f"Pong! `{round((e-s)*1000)}ms`")
