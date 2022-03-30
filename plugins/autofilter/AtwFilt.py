import logging
from pyrogram import Client as illuzX, filters as Worker, emoji
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultCachedDocument
from plugins.database._utils import get_size
from plugins.database.autofilter_db import get_search_results, is_subscribed
from plugins.database.broadcast_db import Database
from config import CACHE_TIME, AUTH_USERS, FORCES_SUB, CUSTOM_FILE_CAPTION , ADMINS
logger = logging.getLogger(__name__)
cache_time = 0 if AUTH_USERS or FORCES_SUB else CACHE_TIME

db = Database()
@illuzX.on_message(Worker.private & Worker.command(["search"]))
async def search_cmd(bot, cmd):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(reply.from_user.id)
    if len(reply.command) != 2:
        if message.from_user.id not in ADMINS: 
            buttons = [[
              InlineKeyboardButton('🔍 Search again 🔎', switch_inline_query_current_chat='')
        ]]
    return InlineKeyboardMarkup(buttons)