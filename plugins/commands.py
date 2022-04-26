from random import choice
from config import START_MSG, FORCES_SUB, BOT_PICS, ADMINS, bot_info, DEV_NAME
from pyrogram import Client as illuzX, filters as Worker
from pyrogram.types import InlineKeyboardMarkup,  InlineKeyboardButton, CallbackQuery
from startup import AtwFilt
from plugins.database.broadcast_db import Database

db = Database()


@illuzX.on_message(Worker.private & Worker.command(["start"]))
async def start_handler(bot, message):
    await message.reply_text(
        text="!!Maintenance!!\nBot Will Be Down For some couple of hours For Maintenance..Will Be UPDATED After Restart",
  )