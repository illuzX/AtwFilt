import re, asyncio, random
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.database._utils import get_size, split_list
from plugins.database.autofilter_db import get_filter_results, get_poster
from config import BUTTONS, bot_info, SPELL_MODE, SET_SPEL_M, SUPPORT, BOT_PICS
from startup import AtwFilt

async def group_filters(client, message):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    if 2 < len(message.text) < 50:    
        btn = []
        search = message.text
        files = await get_filter_results(query=search)
        if files:
            for file in files:
                file_id = file.file_id
                filename = f"{get_size(file.file_size)} {file.file_name}"
                btn.append(
                    [InlineKeyboardButton(text=f"{filename}", callback_data=f"AtwFiltBot#{file_id}")]
                )
        else:
            if SPELL_MODE:
                reply = search.replace(" ", '+')  
                reply_markup = InlineKeyboardMarkup([[
                 InlineKeyboardButton("🎗️ Google 🎗️", url=f"https://www.google.com/search?q={reply}")
                 ],[
                 InlineKeyboardButton("🔍IMDB", url=f"https://www.imdb.com/find?q={reply}"),
                 InlineKeyboardButton("Wikipedia🔎", url=f"https://en.m.wikipedia.org/w/index.php?search={reply}")
                 ]]  
                )    
                atwfiltDl=await message.reply_text(
                    text=SET_SPEL_M.format(query=search, mention=message.from_user.mention),
                    reply_markup=reply_markup                 
                )
                await asyncio.sleep(60) 
                await atwfiltDl.delete()
            return
        if not btn:
            return

        if len(btn) > 10: 
            btns = list(split_list(btn, 10)) 
            keyword = f"{message.chat.id}-{message.id}"
            BUTTONS[keyword] = {
                "total" : len(btns),
                "buttons" : btns
            }
        else:
            buttons = btn
            buttons.append(
                [InlineKeyboardButton(text="📃 Pages 1/1",callback_data="pages"),]
            )

            imdb=await get_poster(search)
            if imdb and imdb.get('poster'):
                dell=await message.reply_photo(photo=imdb.get('poster'), caption=AtwFilt.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(600)
                await dell.delete()
            elif imdb:
                dell=await message.reply_photo(photo=random.choice(BOT_PICS), caption=AtwFilt.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(600)
                await dell.delete()
            else:
                dell=await message.reply_photo(photo=random.choice(BOT_PICS), caption=AtwFilt.GET_MOVIE_2.format(query=search, mention=message.from_user.mention, chat=message.chat.title), reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(600)
                await dell.delete()
            return

        data = BUTTONS[keyword]
        buttons = data['buttons'][0].copy()

        buttons.append(
            [InlineKeyboardButton(text="Next Page ➡",callback_data=f"nextgroup_0_{keyword}")]
        )    
        buttons.append(
            [InlineKeyboardButton(text=f"📃 Pages 1/{data['total']}",callback_data="pages"),]
        )

        imdb=await get_poster(search)
        if imdb and imdb.get('poster'):
            dell=await message.reply_photo(photo=imdb.get('poster'), caption=AtwFilt.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
            await asyncio.sleep(300)
            await dell.delete()        
        elif imdb:
            dell=await message.reply_photo(photo=random.choice(BOT_PICS), caption=AtwFilt.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
            await asyncio.sleep(300)
            await dell.delete()
        else:
            dell=await message.reply_photo(photo=random.choice(BOT_PICS), caption=AtwFilt.GET_MOVIE_2.format(query=search, mention=message.from_user.mention, chat=message.chat.title), reply_markup=InlineKeyboardMarkup(buttons))
            await asyncio.sleep(300)
            await dell.delete()

# ----------tG PM  Module---------- #

async def pm_autofilter(client, message):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    if 2 < len(message.text) < 50:    
        btn = []
        search = message.text
        files = await get_filter_results(query=search)
        if files:
            for file in files:
                file_id = file.file_id
                filename = f"{get_size(file.file_size)} {file.file_name}"
                btn.append(
                    [InlineKeyboardButton(text=f"{filename}", callback_data=f"pmfile#{file_id}")]
                )
        else:
            if SPELL_MODE:
                reply = search.replace(" ", '+')
            await message.reply_text(
                text=AtwFilt.ADD_YOUR_GROUP.format(query=search),
                reply_markup=InlineKeyboardMarkup([[
                   InlineKeyboardButton("🎗️ Google 🎗️", url=f"https://www.google.com/search?q={reply}")
                   ]]
                )
            )
              
            return
        if not btn:
            return

        if len(btn) > 10: 
            btns = list(split_list(btn, 10)) 
            keyword = f"{message.chat.id}-{message.id}"
            BUTTONS[keyword] = {
                "total" : len(btns),
                "buttons" : btns
            }
        else:
            buttons = btn
            buttons.append(
                [InlineKeyboardButton(text="📃 Pages 1/1",callback_data="pages"),]
            )


            imdb=await get_poster(search)
            if imdb and imdb.get('poster'):
                dell=await message.reply_photo(photo=imdb.get('poster'), caption=AtwFilt.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(300)
                await dell.delete()
            elif imdb:
                dell=await message.reply_photo(photo=random.choice(BOT_PICS), caption=AtwFilt.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(300)
                await dell.delete()
            else:
                dell=await message.reply_photo(photo=random.choice(BOT_PICS), caption=AtwFilt.GET_MOVIE_2.format(query=search, mention=message.from_user.mention, chat=bot_info.BOT_NAME), reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(300)
                await dell.delete()

            return

        data = BUTTONS[keyword]
        buttons = data['buttons'][0].copy()

        buttons.append(
            [InlineKeyboardButton(text="Next Page ➡",callback_data=f"nextgroup_0_{keyword}")]
        )    
        buttons.append(
            [InlineKeyboardButton(text=f"📃 Pages 1/{data['total']}",callback_data="pages"),]
        )

        imdb=await get_poster(search)
        if imdb and imdb.get('poster'):
            dell=await message.reply_photo(photo=imdb.get('poster'), caption=AtwFilt.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
            await asyncio.sleep(300)
            await dell.delete()       
        elif imdb:
            dell=await message.reply_photo(photo=random.choice(BOT_PICS), caption=AtwFilt.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
            await asyncio.sleep(300)
            await dell.delete()
        else:
            await message.answer("sorry",show_alert=True)
            
