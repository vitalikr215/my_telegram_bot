from bot import dp
from aiogram import F, html
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from aiogram.utils.formatting import (
    Bold, as_list, as_marked_section, as_key_value, HashTag
)

#/test-markdown - illustrate different approaches to format messages
@dp.message(F.text, Command("test-markdown"))
async def any_message(message: Message):
    await message.answer(
        "This message using <b>HTML</b> markdown", 
        #parse_mode=ParseMode.HTML we could remove this line as we set
        #Default parseMode on Bot constructor
    )
    await message.answer(
        "This message using *Markdown V2*\!", 
        parse_mode=ParseMode.MARKDOWN_V2
    )
    await message.answer(
        "This is <b>without markdown</b>", 
        parse_mode=None
    )

    content = as_list(
        as_marked_section(
            Bold("Success:"),
            "Test 1",
            "Test 3",
            "Test 4",
            marker="✅ ",
        ),
        as_marked_section(
            Bold("Failed:"),
            "Test 2",
            marker="❌ ",
        ),
        as_marked_section(
            Bold("Summary:"),
            as_key_value("Total", 4),
            as_key_value("Success", 3),
            as_key_value("Failed", 1),
            marker="  ",
        ),
        HashTag("#lifestyleblog"),
        sep="\n\n",
    )
    await message.answer(**content.as_kwargs())

#here we illustrate escaping special characters and getting user info
#if user has name for instance <user-name>
@dp.message(Command("hello"))
async def cmd_hello(message: Message):
    await message.answer(f"Hello, {html.bold(html.quote(message.from_user.full_name))}")
