import asyncio,random

CODES=["import hacking...\n[██████████] 100% Complete","Connecting to mainframe...\nAccess Granted ✅","Bypassing firewall...\n[████████░░] 80%"]

async def setup(c):
 from pyrogram import filters
 c.on_message(filters.command("hack",prefixes=".")&filters.me)(h)

async def h(c,m):
 for line in random.choice(CODES).split("\n"):
  await m.edit(line)
  await asyncio.sleep(0.8)
