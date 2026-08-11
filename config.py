import os
from dotenv import load_dotenv
load_dotenv()

API_ID = int(os.getenv("AI_ID"))
API_HASH = os.getenv("API_HASH")
STRING_SESSION = os.getenv("STRING_SESSION")
