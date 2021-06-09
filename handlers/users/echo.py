import os
import re

from aiogram import types
from aiogram.utils.exceptions import FileIsTooBig

from loader import dp, bot
from aiogram.dispatcher import FSMContext
import siaskynet as skynet
from utils import short_link


@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def upload_file(message: types.Message):
    if not os.path.exists('data/temp'):
        os.mkdir('data/temp')

    mess = await message.reply('*Uploading file...*', parse_mode='Markdown')

    try:
        user_id = message.chat.id
        file_name = message.document.file_name
        file = await bot.get_file(message.document.file_id)
        # file_extension = re.search('([0-9a-z]+)(?:[\?#]|$)', message.document.file_name).group(1)
        # print(message.document.file_name)
        # print(file_extension)
        await bot.download_file(file.file_path, f'data/temp/{file_name}')

        client = skynet.SkynetClient()
        url = client.upload_file(f'data/temp/{file_name}', file).replace('sia://', 'https://siasky.net/')
        print('Upload successful: ' + url)
        os.remove(f'data/temp/{file_name}')

        bitly, cuttly, dagb = await short_link(url)

        txt = [
            f'*The file was successfully uploaded.\n',
            f'1. {bitly}',
            f'2. {cuttly}',
            f'4. {dagb}*',
        ]

        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton('🟢 Download file', url=url))

        await mess.edit_text('\n'.join(txt), parse_mode='Markdown', reply_markup=markup, disable_web_page_preview=True)

    except FileIsTooBig:
        await mess.edit_text("*Telegram doesn't support files larger than 20Mb.*", parse_mode='Markdown')


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def no_photo(message: types.Message):
    await message.reply('*Send me an uncompressed photo!*', parse_mode='Markdown')