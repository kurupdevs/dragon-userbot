import asyncio
from pyrogram import Client
from config import API_ID,API_HASH

async def main():
 app=Client("dragon",api_id=API_ID,api_hash=API_HASH)
 await app.start()
 print("Dragon Userbot started!")
 await asyncio.Event().wait()

asyncio.run(main())
