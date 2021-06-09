import os
import re

from aiogram import types
from aiogram.utils.exceptions import FileIsTooBig

from loader import dp, bot
from aiogram.dispatcher import FSMContext
from utils import short_link, ya_upload

allow_users = [486643610, 922942139]


@dp.message_handler(chat_id=allow_users, content_types=types.ContentTypes.DOCUMENT)
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

        url = await ya_upload(f'data/temp/{file_name}', file_name, str(message.chat.id))
        print('Upload successful: ' + url)
        os.remove(f'data/temp/{file_name}')

        txt = [
            f'*The file was successfully uploaded.\n',
            f'{url}*',
        ]

        # markup = types.InlineKeyboardMarkup(row_width=2)
        # markup.add(types.InlineKeyboardButton('🟢 Download file', url=url))

        await mess.edit_text('\n'.join(txt), parse_mode='Markdown', disable_web_page_preview=True)

    except FileIsTooBig:
        await mess.edit_text("*Telegram doesn't support files larger than 20Mb.*", parse_mode='Markdown')


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def no_photo(message: types.Message):
    await message.reply('*Send me an uncompressed photo!*', parse_mode='Markdown')
