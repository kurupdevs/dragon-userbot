import asyncio
from pyrogram import Client
from config import API_ID,API_HASH,BOT_TOKEN

app=Client("dragon",api_id=API_ID,api_hash=API_HASH,bot_token=BOT_TOKEN)

async def main():
 await app.start()
 print("Dragon Userbot running!")
 await asyncio.Event().wait()

if __name__=="__main__":asyncio.run(main())
