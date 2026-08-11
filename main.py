from pyrogram import Client
import os
from modules import *

app = Client(
    "DRAGON-USERBOT",
    pi_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    session_string=os.getenv("SESSION_STRING")
)

import pkgutil, modules
for _, modname, _ in pkgutil.iter_modules(modules.__path__):
    __import__(f"modules.{modname}")

if __name__ == "__main__":
    app.run()
