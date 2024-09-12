from bot import dp
from aiogram.types import Message
from aiogram.types import LinkPreviewOptions
from aiogram.filters.command import Command, CommandObject

#demonstrates all possible options of links preview
@dp.message(Command("links-demo"))
async def cmd_show_links_preview(message: Message):
  links_text = ( "https://upload.wikimedia.org/wikipedia/commons/a/af/Honey_badger.jpg"
        "\n"
        "https://t.me/telegram")
  
  #option with no link preview
  no_preview = LinkPreviewOptions(is_disabled=True)
  await message.answer(f"No links\n {links_text}"
                       ,link_preview_options=no_preview)

  #option with small link preview
  small_preview = LinkPreviewOptions(prefer_small_media=True,
                                      url= "https://upload.wikimedia.org/wikipedia/commons/a/af/Honey_badger.jpg")
  await message.answer(f"Small link preview\n {links_text}"
                       ,link_preview_options=small_preview)
  
  #option with large link preview
  large_preview = LinkPreviewOptions(prefer_large_media=True,
                                      url= "https://upload.wikimedia.org/wikipedia/commons/a/af/Honey_badger.jpg")
  await message.answer(f"Large link preview\n {links_text}"
                       ,link_preview_options=large_preview)
  
  #option with showing small preview above the text
  preview_above_text = LinkPreviewOptions(prefer_small_media=True,
                                      show_above_text= True,
                                      url= "https://upload.wikimedia.org/wikipedia/commons/a/af/Honey_badger.jpg")
  await message.answer(f"Small link preview above the text\n {links_text}"
                       ,link_preview_options=preview_above_text)
  
  #option when you show not specific link preview
  specific_link_preview = LinkPreviewOptions(url="https://t.me/telegram")
  await message.answer(f"Second link preview\n {links_text}"
                       ,link_preview_options=specific_link_preview)
