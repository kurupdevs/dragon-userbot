import time
from pyrogram import Client,filters

ST=time.time()

async def setup(c):c.on_message(filters.command("alive",prefixes=".")&filters.me)(h)

async def h(c,m):
 u=time.time()-ST;h,rem=divmod(u,3600);mn,s=divmod(rem,60)
 await m.edit(f"**Alive!**\nUptime: `{int(h)}h {int(mn)}m {int(s)}s`")
