from bot import dp
from aiogram.filters.command import Command
from aiogram.utils.markdown import hide_link
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.types import Message, LinkPreviewOptions, BufferedInputFile, FSInputFile, URLInputFile


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

#working with album
@dp.message(Command("album"))
async def cmd_album(message: Message):
  album_builder = MediaGroupBuilder(caption="This is a common caption for whole album")
  #album_builder.add(type="photo",media="https://fastly.picsum.photos/id/329/400/300.jpg")
  album_builder.add(type="photo",media=FSInputFile("demo-files/raven.jpg"))
  album_builder.add_photo(media=FSInputFile("demo-files/Honey_badger.jpg"))
  await message.answer_media_group(media=album_builder.build())

#demonstrates possible ways to upload photos
@dp.message(Command("images-demo"))
async def cmd_upload_photo(message: Message):
  file_ids = []

  #sending files from buffer
  with open("demo-files/raven.jpg", "rb") as image_from_buffer:
        result = await message.answer_photo(
            BufferedInputFile(
                image_from_buffer.read(),
                filename="image_from_buffer.jpg"
            ),
            caption="Image from buffer"
        )
        file_ids.append(result.photo[-1].file_id)
  
  #sending files from file system
  image_from_pc = FSInputFile("demo-files/Honey_badger.jpg")
  result = await message.answer_photo(
     image_from_pc,
     caption= "Image from filesystem"
  )
  file_ids.append(result.photo[-1].file_id)

  #sending image from URL (in some reasons does not work)
  #image_from_url = URLInputFile("https://fastly.picsum.photos/id/329/400/300.jpg")
  #result = await  message.answer_photo(
  #   image_from_url,
  #   caption="Image from URL"
  #)
  #file_ids.append(result.photo[-1].file_id)
  #show all ids of uploaded files
  await message.answer("Sent files:\n"+"\n".join(file_ids))

@dp.message(Command("hide-link"))
async def cmd_hidden_link(message:Message):
   message.answer(f"{hide_link('https://telegra.ph/file/562a512448876923e28c3.png')}"
                  f"hide link\n"
                  f"in the text")