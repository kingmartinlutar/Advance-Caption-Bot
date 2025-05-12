from os import environ, getenv
import re
import os

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "5969730414"))
SILICON_PIC = os.environ.get("SILICON_PIC", "https://telegra.ph/file/21a8e96b45cd6ac4d3da6.jpg")
API_ID = int(getenv("API_ID", "25444644"))
API_HASH = str(getenv("API_HASH", "bff60a5f566d9a54c175b0001ba9615b"))
BOT_TOKEN = str(getenv("BOT_TOKEN", "7318084358:AAEULOGdx1s2vJwLg8JWwlbUfkanHG6W-hg"))
FORCE_SUB = os.environ.get("FORCE_SUB", "-1002203710981") 
MONGO_DB = str(getenv("MONGO_DB", "mongodb+srv://replacewithyourmongodb:replacewithyourmongodb@cluster0.zi78j51.mongodb.net/?retryWrites=true&w=majority",))
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b>File Name:- `{file_name}`\n\n{file_size}</b>",
    )
)
