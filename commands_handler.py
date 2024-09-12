from bot import dp
from aiogram.types import Message
from aiogram.filters.command import Command, CommandObject

#demostrate how to work with commands with several arguments
@dp.message(Command("settimer"))
async def cmd_settimer(message: Message, command: CommandObject):
    if command.args is None:
        await message.answer("Error: arguments not provided")
    try:
        delay_time, text_to_send = command.args.split(" ", maxsplit=1)
    except:
        await message.answer("Error: incorrect format\n"
                             "/settimer <time> <message>")
        return
    await message.answer(f"Timer was added !\n"
                         f"Time: {delay_time}\n"
                         f"Message: {text_to_send}\n")
