from aiogram.types import Message,ReplyKeyboardMarkup
from loader import dp


@dp.message_handler(text="1video")
async def show_menu(message:Message):
    await message.answer("https://vt.tiktok.com/ZSNsk5GUd/")

@dp.message_handler(text="2video")
async def show_menu(message:Message):
    await message.answer("https://vt.tiktok.com/ZSNskYapT/")

@dp.message_handler(text="3video")
async def show_menu(message:Message):
    await message.answer("https://vt.tiktok.com/ZSNsk5uAA/")
