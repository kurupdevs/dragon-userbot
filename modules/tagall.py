import asyncio

async def setup(c):
 from pyrogram import filters
 c.on_message(filters.command("tagall",prefixes=".")&filters.me)(h)

async def h(c,m):
 t=m.text.split(None,1)[1]if len(m.text.split())>1 else"Attention!"
 await m.delete()
 ms=[];async for mb in c.get_chat_members(m.chat.id):
  if not mb.user.is_bot:ms.append(mb.user.mention)
  if len(ms)>=5:await c.send_message(m.chat.id,f"{t} {' '.join(ms)}");ms=[];await asyncio.sleep(0.5)
 if ms:await c.send_message(m.chat.id,f"{t} {' '.join(ms)}")
