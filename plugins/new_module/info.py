# © illuzx

import shutil
import psutil
import config
#import client 
from plugins.database.autofilter_db import Media
from config import ADMINS
from pyrogram import Client as illuzx, filters ,enums
from pyrogram.types import (
    Message
)
#import Db Uri **To Know How Many Users (db)
from plugins.database.users_chats_db import db
from plugins.new_module.run_cb import humanbytes
@illuzx.on_message(filters.command("status") & filters.user(config.ADMINS))
async def status_handler(_, m: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory ().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count ()
    files = await Media.count_documents()
    await m.reply_text(
        text=f"**Total Files:** {files} \n\n"
             f"**Total Disk Space:** {total} \n"
             f"**Used Space:** {used}({disk_usage}%) \n"
             f"**Free Space:** {free} \n"
             f"**Cpu Usage:** {cpu_usage}% \n"
             f"**Ram Usage:** {ram_usage}%\n"
             f"**Total Users In db:** {total_users}`",
        parse_mode=enums.ParseMode.MARKDOWN,
        quote=True
        )
