import datetime
from bot import dp #importing dispatcher
from aiogram import types
from aiogram.filters.command import Command, CommandObject
import aiogram.types
from aiogram.enums.dice_emoji import DiceEmoji

# /start command handler
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    now = datetime.datetime.now()
    #formatedNow = now.strftime("%Y-%m-%d %H:%M:%S")
    await message.answer("Hello, you started bot at "+now.strftime("%Y-%m-%d %H:%M:%S") +" !")

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