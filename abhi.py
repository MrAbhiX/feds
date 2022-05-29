from pyrogram import Client 
from Config import Config

ABHI = Client(
    api_hash=Config.API_HASH,
    api_id=Config.APP_ID,
    session_name=Config.STRING_SESSION,
    sleep_threshold=10
)
