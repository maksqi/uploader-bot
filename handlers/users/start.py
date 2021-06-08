from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        '*This bot provides a public URL to files in Telegram.\nIt accepts photo, gif, video, audio, voice and other documents*',
        parse_mode='Markdown')
