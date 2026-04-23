import asyncio
import importlib
from sys import argv
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from KrishNetwork import LOGGER, app, userbot
from KrishNetwork.core.call import Hotty
from KrishNetwork.misc import sudo
from KrishNetwork.plugins import ALL_MODULES
from KrishNetwork.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    
    await sudo()
    
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass

    # 1. Main Bot Start karein
    await app.start()
    LOGGER("KrishNetwork").info("Main Bot Started. Waiting for 5 seconds...")
    await asyncio.sleep(5) # Thoda intezar taaki flood na ho

    # 2. Plugins Load karein
    for all_module in ALL_MODULES:
        importlib.import_module("KrishNetwork.plugins" + all_module)
    LOGGER("KrishNetwork.plugins").info("Successfully Imported Modules...")

    # 3. Assistant Start karein
    await userbot.start()
    LOGGER("KrishNetwork").info("Assistant Started. Waiting for 5 seconds...")
    await asyncio.sleep(5) # Phir se thoda intezar

    # 4. PyTgCalls (Hotty) Start karein
    await Hotty.start()
    
    try:
        await Hotty.stream_call("https://graph.org/file/e999c40cb700e7c684b75.mp4")
    except NoActiveGroupCall:
        LOGGER("KrishNetwork").error(
            "Please turn on the videochat of your log group/channel.\n\nStopping Bot..."
        )
        exit()
    except Exception as e:
        LOGGER("KrishNetwork").error(f"Stream Error: {e}")

    await Hotty.decorators()
    LOGGER("KrishNetwork").info("Stark-Tech Music System is now Online! 🦾")
    
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("KrishNetwork").info("Stopping KrishNetwork Music Bot...")

if __name__ == "__main__":
    # Event loop setup with improved error handling
    try:
        asyncio.get_event_loop().run_until_complete(init())
    except KeyboardInterrupt:
        pass
        
