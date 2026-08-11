import os, asyncio, glob, importlib
from pyrogram import Client, idle

app = Client(
    "DRAGON-USERBOTx",
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
    session_string=os.environ["STRING_SESSION"]
)

for file in glob.glob("modules/*.py"):
    importlib.import_module(file.replace("/", ".")[:-3])

print("🐉 DRAGON-USERBOT (Userbot Mode) is alive!")
app.start()
idle()
app.stop()
