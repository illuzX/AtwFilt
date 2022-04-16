import re
from os import environ
from startup import AtwFilt
id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "on"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "off"]:
        return False
    else:
        return default

# ==================================
API_ID = int(environ["API_ID"])
API_HASH = environ["API_HASH"]
B_KEYS = environ["BOT_TOKEN"]
START_MSG = environ.get("START_MSG",AtwFilt.DEFAULT_MSG)
BOT_PICS = (environ.get('PICS', 'https://telegra.ph/file/d5074341e29977da5ae60.jpg https://telegra.ph/file/5687297fe4b13efa8d595.jpg')).split()
SUPPORT = environ.get("SUPPORT", "https://www.google.com")
SPELL_MODE = is_enabled((environ.get('SPELL_MODE', "on")), True)
SET_SPEL_M = environ.get("SPELL_MODE_TEXT",AtwFilt.SPELL_CHECK)
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", -1001645658297))
DATABASE_URI = environ.get("DATABASE_URI", None)
FORCE = environ.get('FORCES_SUB')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", AtwFilt.FILE_CAPTIONS)
DEV_NAME = environ.get("DEV_NAME", "Illuzx")
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', "").split()]


# ==================================
# Empty 😂
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
CACHE_TIME = int(environ.get('CACHE_TIME', 60))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
BUTTONS = {}
CURRENT = int(environ.get("SKIP", 2))
CANCEL = False
FORCES_SUB = int(FORCE) if FORCE and id_pattern.search(FORCE) else FORCE
DATABASE_NAME = environ.get("DATABASE_NAME", 'UserStorage2')
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
# ==================================

team_name = os.environ.get('team_name','TeamCode')
team_link = os.environ.get('team_link', 't.me/grayhathacker767'):

# ==================================
# ==================================
# About Bot 🤖
class bot_info(object):
    BOT_NAME = None
    BOT_USERNAME = None
    BOT_ID = None

