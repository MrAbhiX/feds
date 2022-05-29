import asyncio
import logging
from Config import Config
from pyrogram import idle
from Abhi import ABHI

logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pyrogram.session.session").setLevel(logging.ERROR)
logging.getLogger("pyrogram.parser.html").setLevel(logging.ERROR)


async def main_startup():
    print("""
|| abhi Userbot ||
Copyright (c) 2021 MrAbhiX
"""
    )
    await ABHI.start()
    try:
        await ABHI.send_message(chat_id=Config.LOG_GROUP, text="**Abhi Userbot is alive!**")
    except:
        logging.warn("There was an error while creating the LOG CHANNEL please add a one manually!")
    logging.info("\n\n ✨ Abhi Userbot is Alive \n\n")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(main_startup())
