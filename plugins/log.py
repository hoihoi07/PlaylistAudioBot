# HuzunluArtemis - 2021 (Licensed under GPL-v3)

from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message
from HelperFunc.messageFunc import sendDocument
import logging
from config import Config
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


@Client.on_message(filters.command(Config.LOG_COMMAND))
def log(bot, message:Message):
    if not (Config.OWNER_ID != 0 and message.from_user.id == Config.OWNER_ID): return
    sendDocument(message,"log.txt")
