import logging
from pyrogram import Client as illuzX, filters as Worker
from plugins.database.autofilter_db import Media
from config import ADMINS
logger = logging.getLogger(__name__)

@illuzX.on_message(Worker.command('myDb') & Worker.user(ADMINS))
async def total(bot, message):

    msg = await message.reply("Processing...⏳", quote=True)
    try:
        total_users = await db.total_users_count()
    files = await Media.count_documents()
    size = await db.get_db_size()
    free = 536870912 - size
    size = get_size(size)
    free = get_size(free)
    await rju.edit(startup.STATUS_TXT.format(files, total_users, totl_chats, size, free)),
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')
