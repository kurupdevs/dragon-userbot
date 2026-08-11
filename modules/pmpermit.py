import asyncio
from pyrogram import Client,filters

BLOCKED=set()

async def setup(c):
 c.on_message(filters.private&~filters.me)(chk)
 c.on_message(filters.command("pmpermit",prefixes=".")&filters.me)(tog)

async def chk(c,m):
 if m.from_user.id in BLOCKED:await m.reply("PM blocked.")

async def tog(c,m):
 t=m.reply_to_message.from_user.id if m.reply_to_message else None
 if t:
  if t in BLOCKED:BLOCKED.discard(t);await m.edit("Unblocked")
  else:BLOCKED.add(t);await m.edit("Blocked")
