# (c) @biisal
from os import getenv
import re

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "6233910543"))
API_ID = int(getenv("API_ID", "20919625"))
API_HASH = str(getenv("API_HASH", "40168846bf06f4ff443f0f7a4182bf8d"))
BOT_TOKEN = str(getenv("BOT_TOKEN", ""))
MONGO_DB = str(
    getenv(
        "MONGO_DB",
        "mongodb+srv://replacewithyourmongodb:replacewithyourmongodb@cluster0.zi78j51.mongodb.net/?retryWrites=true&w=majority",
    )
)
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b><a href='telegram.me/bisal_files'>{file_name} Telegram : @Bisal_Files\n\nForward the file before Downloading.</a></b>",
    )
)
