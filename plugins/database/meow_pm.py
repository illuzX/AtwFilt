import logging
from pyrogram.errors import InputUserDeactivated, UserNotParticipant, FloodWait, UserIsBlocked, PeerIdInvalid
import asyncio
from pyrogram.types import Message
from typing import Union
import re
import os
from datetime import datetime
from typing import List
from pyrogram.types import InlineKeyboardButton
from plugins.database.users_chats_db import db
from bs4 import BeautifulSoup
import requests
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# temp db for banned 
class temp(object):
    BANNED_USERS = []
    BANNED_CHATS = []
    ME = None
    CURRENT=int(os.environ.get("SKIP", 2))
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None
    SETTINGS = {}
