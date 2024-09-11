#address of my bot https://t.me/first_vitalik_telegram_bot
import asyncio
import datetime
import logging

import config

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
from aiogram.enums.dice_emoji import DiceEmoji

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.BOT_TOKEN)

dp = Dispatcher()
#if need to pass some params for bot for lifetime
dp["started_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
dp["version"] = config.BOT_VERSION 

# /start command handler
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    now = datetime.datetime.now()
    #formatedNow = now.strftime("%Y-%m-%d %H:%M:%S")
    await message.answer("Hello from "+now.strftime("%Y-%m-%d %H:%M:%S") +" !")

#/answer command handler
@dp.message(Command("answer"))
async def cmd_answer(message: types.Message):
    await message.answer("This is just answer from the bot")

#/reply command handler
@dp.message(Command("reply"))
async def cmd_reply(message: types.Message):
    await message.reply("This is reply to your message")

#/dice
@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)
    #to send the same dice to specific channel (first argument is a channel id)
    #await bot.send_dice(-100123456789, emoji=DiceEmoji.DICE)

#/info
@dp.message(Command("info"))
async def cmd_info(message: types.Message, started_at: str, version: str):
    await message.answer(f"Bot version={version} started at {started_at}")

#/add-to-list
@dp.message(Command("add-to-list"))
async def cmd_add_to_list(message: types.Message, command: CommandObject, mylist: list[int]):
    mylist.append(int(command.args))
    await message.answer(f"Added {command.args} to list")    

#/show-list
@dp.message(Command("show-list"))
async def cmd_add_to_list(message: types.Message, mylist: list[int]):    
    await message.answer(f"Your list: {mylist}")    


# polling new updates from Telegram
async def main():
    print("Bot version:"+config.BOT_VERSION)
    #add some initial object for bot
    await dp.start_polling(bot,mylist=[1, 2, 3])

if __name__ == "__main__":
    asyncio.run(main())