import logging
from pyrogram import Client as illuzX, filters as Worker
from plugins.database.autofilter_db import Media

from config import ADMINS
logger = logging.getLogger(__name__)

@illuzX.on_message(Worker.command('myDb') & Worker.user(ADMINS))
async def total(bot, message):

    msg = await message.reply("please wait...⏳️"
 quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f'📁𝕋𝕠𝕥𝕒𝕝 𝕊𝕒𝕧𝕖𝕕 𝔽𝕚𝕝𝕖𝕤 𝕀𝕟 𝔻𝕒𝕥𝕒𝕓𝕒𝕤𝕖🌸: {total}')
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')
