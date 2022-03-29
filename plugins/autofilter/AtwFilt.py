import logging
from pyrogram import Client as illuzX, filters as Worker, emoji
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultCachedDocument
from plugins.database._utils import get_size
from plugins.database.autofilter_db import get_search_results, is_subscribed
from config import CACHE_TIME, AUTH_USERS, FORCES_SUB, CUSTOM_FILE_CAPTION
logger = logging.getLogger(__name__)
cache_time = 0 if AUTH_USERS or FORCES_SUB else CACHE_TIME

@illuzX.on_message(Worker.command('Srch') & Worker.user(AUTH_USERS) if AUTH_USERS else None)
def get_reply_markup(query):
    buttons = [[
              InlineKeyboardButton('🔍 Search again 🔎', switch_inline_query_current_chat='')
        ]]
    return InlineKeyboardMarkup(buttons)