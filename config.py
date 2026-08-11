"""Dragon Userbot Configuration."""

import os
from environs import Env

env = Env()
env.read_env()

API_ID = env.int("API_ID", 0)  # type: int
API_HASH = env.str("API_HASH", "")  # type: str
PREFIX = env.str("PREFIX", ".")  # type: str
