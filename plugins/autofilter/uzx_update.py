# Search + And + Get + How + To + Use 
# Search + Inline Mode / Hint 
#from pyrogram import Client as illuzX, filter 
#@illuz
from config import START_MSG, FORCES_SUB, BOT_PICS, ADMINS, bot_info, DEV_NAME
from pyrogram import Client as illuzX, filters as Worker
from pyrogram.types import InlineKeyboardMarkup,  InlineKeyboardButton, CallbackQuery
from startup import AtwFilt
from plugins.database.broadcast_db import Database

db = Database()


@illuzX.on_message(Worker.private & Worker.command(["search"]))
async def search_mesaage(bot, message):
  if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(LOG_CHANNEL, startup.LOG_CB.format(message.from_user.id, message.from_user.mention))
       else:
            buttons = [
             InlineKeyboardButton("🔎𝚂𝚎𝚊𝚛𝚌𝚑",switch_inline_query_current_chat='')
             ]