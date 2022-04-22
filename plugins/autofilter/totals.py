import logging
import shutil
import psutil
from pyrogram import Client as illuzX, filters as Worker
from plugins.database.autofilter_db import Media
from config import ADMINS
from plugins.Addmin.runner import humanbytes
logger = logging.getLogger(__name__)


@illuzX.on_message(Worker.command("status") & Worker.user(ADMINS) & ~Worker.edited)
async def status(bot,  Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    await m.reply_text(
        text=f"**Total Disk Space:** {total} \n"
             f"**Used Space:** {used}({disk_usage}%) \n"
             f"**Free Space:** {free} \n"
             f"**CPU Usage:** {cpu_usage}% \n"
             f"**RAM Usage:** {ram_usage}%\n\n",
        parse_mode="Markdown",
        quote=True
    )