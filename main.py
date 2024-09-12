#address of my bot https://t.me/first_vitalik_telegram_bot
import bot
import basic_handlers
import markdown_handlers
import asyncio
import logging

# polling new updates from Telegram
async def main():
    #await misc.dp.start_polling(misc.bot, allowed_updates=misc.dp.resolve_used_update_types())
    #add some initial object for bot
    await bot.dp.start_polling(bot.bot,mylist=[1, 2, 3])


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())