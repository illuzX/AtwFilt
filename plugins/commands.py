from random import choice
from config import START_MSG, FORCES_SUB, BOT_PICS, ADMINS, bot_info, DEV_NAME
from pyrogram import Client as illuzX, filters as Worker
from pyrogram.types import InlineKeyboardMarkup,  InlineKeyboardButton, CallbackQuery
from startup import AtwFilt
from plugins.database.broadcast_db import Database

db = Database()


@illuzX.on_message(Worker.private & Worker.command(["start"]))
async def start_message(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
    if len(message.command) != 2:
        if message.from_user.id not in ADMINS: 
            buttons = [[
             InlineKeyboardButton("🔍 𝐬𝐞𝐚𝐫𝐜𝐡 🔎", switch_inline_query_current_chat='')
            ] ,[
             InlineKeyboardButton("🔰𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥🔰", url="https://t.me/MalayalamOTTUpdatesMvb")
            ] ,[
             InlineKeyboardButton("🔸𝐌𝐨𝐯𝐢𝐞𝐬 𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥🔸", url="https://t.me/mvbzzer")
             ]]
        else:
            buttons = [[
             InlineKeyboardButton("🔍 𝐬𝐞𝐚𝐫𝐜𝐡 🔎", switch_inline_query_current_chat='')
          ] ,[
             InlineKeyboardButton("🔰𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥🔰", url="https://t.me/MalayalamOTTUpdatesMvb")
          ] ,[
             InlineKeyboardButton("🔸𝐌𝐨𝐯𝐢𝐞𝐬 𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥🔸", url="https://t.me/mvbzzer")
             ]]    
        await message.reply_photo(photo = choice(BOT_PICS), caption=AtwFilt.DEFAULT_MSG.format(mention = message.from_user.mention, bot_name = bot_info.BOT_NAME, bot_username = bot_info.BOT_USERNAME), reply_markup=InlineKeyboardMarkup(buttons))
        
    elif len(message.command) ==2 and message.command[1] in ["subscribe"]:
        FORCES=["https://telegra.ph/file/10e57b92fde7aa7b540cf.jpg"]
        invite_link = await bot.create_chat_invite_link(int(FORCES_SUB))
        button=[[
         InlineKeyboardButton("🦋Join To Use Me", url=invite_link.invite_link)
         ]]
        reply_markup = InlineKeyboardMarkup(button)
        await message.reply_photo(
            photo=choice(FORCES),
            caption=f"""<i><b>Hello {message.from_user.mention}. \nYou Have <a href="{invite_link.invite_link}">Not Join</a> To <a href="{invite_link.invite_link}">My Update Channel</a>.So you do not get access To Files on Inline Mode, Bot Pm and Group</i></b>""",
            reply_markup=reply_markup
        )
        return
   
@illuzX.on_message(Worker.private & Worker.command(["help"]))
async def help(bot, message):
    button = [[
     InlineKeyboardButton("source code", callback_data="SOURCE_CODE"),
     InlineKeyboardButton("About 😎", callback_data="about")
     ]]
    await message.reply_photo(
        photo = choice(BOT_PICS),
        caption=AtwFilt.HELP_MSG.format(mention=message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(button))
      
@illuzX.on_message(Worker.private & Worker.command(["about"]))
async def about(bot, message):
    button = [[
     InlineKeyboardButton("🏠 Home", callback_data="start"),
     InlineKeyboardButton("Close 🗑️", callback_data="close")
     ]]  
    await message.reply_photo(
        photo = choice(BOT_PICS),
        caption=AtwFilt.ABOUT_MSG.format(mention=message.from_user.mention, bot_name=bot_info.BOT_NAME, bot_username=bot_info.BOT_USERNAME, dev_name=DEV_NAME),
        reply_markup=InlineKeyboardMarkup(button))
        
