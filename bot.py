import datetime
import config
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

bot = Bot(default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    token=config.BOT_TOKEN)

dp = Dispatcher()
#if need to pass some params for bot for lifetime
dp["started_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
dp["version"] = config.BOT_VERSION