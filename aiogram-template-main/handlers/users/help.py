from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/info_html - html tegs",
            "/user_id - shaxs id",
            "/menu - bosh menu")

    await message.answer("\n".join(text))
