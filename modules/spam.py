import asyncio
from pyrogram import Client,filters

async def setup(c):
 c.on_message(filters.command("spam",prefixes=".")&filters.me)(sp)
 c.on_message(filters.command("purge",prefixes=".")&filters.me)(pu)

async def sp(c,m):
 a=m.text.split(None,2)
 if len(a)<3:await m.edit("Usage: .spam <count> <text>");return
 try:count=min(int(a[1]),50)
 except:await m.edit("Invalid");return
 await m.delete()
 for _ in range(count):await c.send_message(m.chat.id,a[2]);await asyncio.sleep(0.4)

async def pu(c,m):
 if not m.reply_to_message:await m.edit("Reply to start.");return
 cid=m.chat.id;s=m.reply_to_message.id;e=m.id
 await m.delete();d=0
 for mid in range(s,e+1):
  try:await c.delete_messages(cid,mid);d+=1
  except:pass
 st=await c.send_message(cid,f"Purged {d} msgs.")
 await asyncio.sleep(3);await st.delete()
