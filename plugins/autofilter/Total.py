import logging
from pyrogram import Client as illuzX, filters as Worker
from plugins.database.autofilter_db import Media
from plugins.database.user_chat_db import db

from config import ADMINS
logger = logging.getLogger(__name__)

@illuzX.on_message(Worker.command('myDb') & Worker.user(ADMINS))
async def total(bot, message):

    msg = await message.reply("LoOdIng...⏳🌸", quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f'📁 Saved files: {total}')
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')