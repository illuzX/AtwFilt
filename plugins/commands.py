from random import choice
from config import START_MSG, FORCES_SUB, BOT_PICS, ADMINS, bot_info, DEV_NAME
from pyrogram import Client as illuzX, filters as Worker
from pyrogram.types import InlineKeyboardMarkup,  InlineKeyboardButton, CallbackQuery
from startup import AtwFilt
from plugins.database.broadcast_db import Database

db = Database()


@illuzX.on_message(Worker.private & Worker.command(["start"]))
async def start_message(bot, message):
        await message.reply_photo(photo = choice(BOT_PICS), caption=START_MSG.format(mention = message.from_user.mention, bot_name = bot_info.BOT_NAME, bot_username = bot_info.BOT_USERNAME)