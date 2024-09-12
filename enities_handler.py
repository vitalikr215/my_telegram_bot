#demonstrate working with entities
#if need to parse message in our example get email, url, and code (password)
from bot import dp
from aiogram import F, html
from aiogram.types import Message

@dp.message(F.text)
async def extract_cred_data(message: Message):
    data = {
        "url":"N/A",
        "email":"N/A",
        "code" : "N/A"
    }

    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            data[item.type] = item.extract_from(message.text)
    
    await message.reply(
        "Parsing your message I've found:\n"
        f"URL: {html.quote(data['url'])}\n"
        f"E-mail: {html.quote(data['email'])}\n"
        f"Password: {html.quote(data['code'])}\n"
    )