import asyncio
import random
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from KrishNetwork import app
from KrishNetwork.utils.database import get_served_chats, get_served_users

# --- Security: Your Fixed ID ---
ACTUAL_OWNER = 7081885854

# --- Aggressive Roast List ---
ROAST_MESSAGES = [
    "Fuck off, you pathetic piece of shit! Don't touch my Master's commands.",
    "Get the fuck out of here! You're nothing but a low-life beggar trying to steal my bot.",
    "Shut your dirty mouth and get lost! Only my real Owner (7081885854) can control me.",
    "Go cry to your mother, you loser! You don't have the balls to use this command.",
    "Hey asshole, stay in your limits! One more try and I'll kick your soul out of this group.",
    "You goddamn thief! Stop trying to promote your trash here and fuck off!",
    "Error 404: Your dignity not found. Stop acting like a boss, you little bitch!"
]

# --- Fast Broadcast Function ---
async def send_msg(chat_id, message):
    try:
        await message.copy(chat_id)
        return True
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await send_msg(chat_id, message)
    except:
        return False

# --- Main Command ---
@app.on_message(filters.command(["broadcast", "gcast"]))
async def fast_broadcast(client, message: Message):
    # Security Check
    if message.from_user.id != ACTUAL_OWNER:
        roast = random.choice(ROAST_MESSAGES)
        return await message.reply_text(f"**{roast}**")

    if not message.reply_to_message:
        return await message.reply_text("❌ **Master, please reply to a message!**")

    status_msg = await message.reply_text("⚡ **ғᴀsᴛ ʙʀᴏᴀᴅᴄᴀsᴛ sᴛᴀʀᴛɪɴɢ...**")
    
    served_chats = await get_served_chats()
    served_users = await get_served_users()
    all_targets = [int(chat["chat_id"]) for chat in served_chats]
    all_targets.extend([int(user["user_id"]) for user in served_users])

    sent = 0
    failed = 0
    
    batch_size = 10 
    for i in range(0, len(all_targets), batch_size):
        batch = all_targets[i : i + batch_size]
        tasks = [send_msg(chat_id, message.reply_to_message) for chat_id in batch]
        results = await asyncio.gather(*tasks)
        for res in results:
            if res: sent += 1
            else: failed += 1
        await asyncio.sleep(0.1)

    await status_msg.edit_text(
        f"🚀 **ᴜʟᴛʀᴀ ғᴀsᴛ ʙʀᴏᴀᴅᴄᴀsᴛ ᴅᴏɴᴇ!**\n\n"
        f"✅ **sᴇɴᴛ:** `{sent}`\n"
        f"❌ **ғᴀɪʟᴇᴅ:** `{failed}`\n"
        f"**Master, the work is done!**"
    )
    
