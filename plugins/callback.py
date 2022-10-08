from pyrogram import Client as illuzX, filters as Worker
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserIsBlocked, PeerIdInvalid
from plugins.database.autofilter_db import  get_file_details
from plugins.database._utils import get_size, is_subscribed
from startup import AtwFilt
from config import BUTTONS, FORCE_SUB, CUSTOM_FILE_CAPTION, START_MSG, DEV_NAME, bot_info, ADMINS


@illuzX.on_callback_query()
async def cb_handler(client: illuzX, query):
    clicked = query.from_user.id
    try:
        typed = query.message.reply_to_message.from_user.id
    except:
        typed = query.from_user.id

    if (clicked == typed):


# # ---------- 🔘 [ | 𝗚𝗥𝗢𝗨𝗣 𝗙𝗜𝗟𝗧𝗘𝗥𝗦 | ] 🔘 ---------- # #

        if query.data.startswith("nextgroup"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again 🙏",show_alert=True)
                return

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton(" Back Page", callback_data=f"backgroup_{int(index)+1}_{keyword}")
                    ]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)+2}/{data['total']}", callback_data="pages"),]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton(" Back Page", callback_data=f"backgroup_{int(index)+1}_{keyword}"),InlineKeyboardButton("Next Page ➡", callback_data=f"nextgroup_{int(index)+1}_{keyword}")
                    ]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)+2}/{data['total']}", callback_data="pages"),]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

        elif query.data.startswith("backgroup"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again 🙏",show_alert=True)
                return

            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("Next Page ➡", callback_data=f"nextgroup_{int(index)-1}_{keyword}")
                    ]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)}/{data['total']}", callback_data="pages"),]
                )
                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton(" Back Page", callback_data=f"backgroup_{int(index)-1}_{keyword}"),InlineKeyboardButton("Next Page ➡", callback_data=f"nextgroup_{int(index)-1}_{keyword}")
                    ]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)}/{data['total']}", callback_data="pages"),]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

# # ---------- 🔘 [ | 𝗕𝗢𝗧 𝗣𝗠 𝗙𝗜𝗟𝗧𝗘𝗥𝗦 | ] 🔘 ---------- # #


        elif query.data.startswith("nextbot"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again 🙏",show_alert=True)
                return

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton(" Back Page", callback_data=f"backbot_{int(index)+1}_{keyword}")
                    ]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)+2}/{data['total']}", callback_data="pages"),]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton(" Back Page", callback_data=f"backbot_{int(index)+1}_{keyword}"),InlineKeyboardButton("Next Page ➡", callback_data=f"nextbot_{int(index)+1}_{keyword}")
                    ]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)+2}/{data['total']}", callback_data="pages"),]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

        elif query.data.startswith("backbot"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again 🙏",show_alert=True)
                return

            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("Next Page ➡", callback_data=f"nextbot_{int(index)-1}_{keyword}")
                    ]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)}/{data['total']}", callback_data="pages"),]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()
                
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)}/{data['total']}", callback_data="pages"),]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

# ---------- 📁 [ | 𝗚𝗘𝗧 𝗙𝗜𝗟𝗘𝗦 | ] 📁 ---------- #


        elif query.data.startswith("AtwFilt"):
            ident, file_id = query.data.split("#")
            files_ = await get_file_details(file_id)
            if not files_:
                return await query.answer('No such file exist.')
            files = files_[0]
            title = files.file_name
            size=get_size(files.file_size)
            caption=CUSTOM_FILE_CAPTION.format(mention=query.from_user.mention, title=title, size=size, caption=files.caption)

            try:
                if FORCE_SUB and not await is_subscribed(client, query):
                    await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")
                    return
                else:
                    await client.send_cached_media(
                        chat_id=query.from_user.id,
                        file_id=file_id,
                        caption=caption
                        )
                    await query.answer('🤖 Check PM, I have Sent Files In Pm 🤖',show_alert = True)
            except UserIsBlocked:
                await query.answer('Unblock the bot mahn !',show_alert = True)
            except PeerIdInvalid:
                await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")
            except Exception as e:
                await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")

# ---------- 📁 [ | 𝗣𝗠 𝗙𝗜𝗟𝗘𝗦 | ] 📁 ---------- #

        elif query.data.startswith("pmfile"):
            if FORCE_SUB and not await is_subscribed(client, query):
                await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")
                return
            ident, file_id = query.data.split("#")
            filedetails = await get_file_details(file_id)
            for files in filedetails:
                title = files.file_name
                size=get_size(files.file_size)
                
                caption=CUSTOM_FILE_CAPTION.format(mention=query.from_user.mention, title=title, size=size, caption=files.caption)

                buttons = [[
                  InlineKeyboardButton('📍Mᴀɪɴ ᴄʜᴀɴɴᴇʟ📌', url='https://t.me/Mvbzzer'),
                  InlineKeyboardButton("🔎Sᴇᴀʀᴄʜ Aɢᴀɪɴ 📌",switch_inline_query_current_chat='')
                  ],[
                  InlineKeyboardButton("🌸Dᴀᴛᴀʙᴀsᴇ🌸", url='https://t.me/Files_For_Bot')
                  ]]
                
                await query.answer()
                await client.send_cached_media(
                    chat_id=query.from_user.id,
                    file_id=file_id,
                    caption=caption,
                    reply_markup=InlineKeyboardMarkup(buttons)
                    )


# ---------- 📁 [ | 𝗠𝗢𝗗𝗨𝗟𝗘𝗦 | ] 📁 ---------- #


        elif query.data == "start":
            if query.from_user.id not in ADMINS: 
                buttons = [[
                 InlineKeyboardButton("Aʙᴏᴜᴛ  🦜" , callback_data="about"),
                 InlineKeyboardButton("Sᴇᴀʀᴄʜ Mᴏᴠɪᴇ🔎", switch_inline_query_current_chat='')
                ], [
                 InlineKeyboardButton("⚙️ BᴏT Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ⚙️", url="https://t.me/mvbzzer")
                ], [
                 InlineKeyboardButton("Hᴏᴡ Tᴏ Usᴇ Mᴇ ❓ " , url="https://t.me/+2QLvbzUUdB8yNjM1")
                 ]]
            else:
                buttons = [[
                 InlineKeyboardButton("Aʙᴏᴜᴛ  🦜" , callback_data="about"),
                 InlineKeyboardButton("Sᴇᴀʀᴄʜ Mᴏᴠɪᴇ🔎", switch_inline_query_current_chat='')
                ], [
                 InlineKeyboardButton("⚙️ BᴏT Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ⚙️", url="https://t.me/mvbzzer")
                ], [
                 InlineKeyboardButton("Hᴏᴡ Tᴏ Usᴇ Mᴇ ❓ ",  url="https://t.me/+2QLvbzUUdB8yNjM1")
                 ]]               
            await query.message.edit(text=AtwFilt.START_TXT.format(mention=query.from_user.mention, bot_name=bot_info.BOT_NAME, bot_username=bot_info.BOT_USERNAME), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=False)

        elif query.data == "help":
            buttons = [[
              InlineKeyboardButton("source code ", callback_data="SOURCE_CODE"),
              InlineKeyboardButton("About 😎", callback_data="about")
              ]]               
            await query.message.edit(text=AtwFilt.HELP_MSG.format(mention=query.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=False)

        elif query.data == "about":
            buttons = [[
             InlineKeyboardButton("Back", callback_data="start"),
             InlineKeyboardButton("Close 🗑️", callback_data="close")
             ]]               
            await query.message.edit(text=AtwFilt.ABOUT_MSG.format(mention=query.from_user.mention, bot_name=bot_info.BOT_NAME, bot_username=bot_info.BOT_USERNAME, dev_name=DEV_NAME), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=False)

        elif query.data == "close":
            await query.message.delete()

        elif query.data == "bot_owner":
            buttons = [[
             InlineKeyboardButton('source code', callback_data="SOURCE_CODE"),
             InlineKeyboardButton('About 😎', callback_data="about")
             ]]               
            await query.message.edit(text=AtwFilt. illuzX.format(mention=query.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)
        elif query.data == "SOURCE_CODE":
            buttons = [[
             InlineKeyboardButton('BACK', callback_data="start"),
             InlineKeyboardButton('About 😎', callback_data="about")
             ]]
            await query.message.edit(text=AtwFilt.SOURCE_CODE.format(mention=query.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=False)
            
        elif query.data == "pages":
            await query.answer()

        elif query.data == "close":
            await query.message.delete()

    else:
        await query.answer("Please Request",show_alert=True)
