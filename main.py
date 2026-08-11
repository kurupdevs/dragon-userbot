import os,asyncio,logging
from pyrogram import Client

logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger=logging.getLogger(__name__)
app=Client("dragon",api_id=int(os.getenv("API_ID",0)),api_hash=os.getenv("API_HASH",""))

async def main():
 try:
  logger.info("Starting Dragon...")
  await app.start()
  logger.info("Dragon running!")
  await asyncio.Event().wait()
 except Exception as e:logger.error(f"Fatal: {e}")

if __name__=="__main__":asyncio.run(main())
