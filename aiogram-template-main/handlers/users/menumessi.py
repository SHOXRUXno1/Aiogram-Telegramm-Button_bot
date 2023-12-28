from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from keyboards.default.forMessi import menuMessi
from keyboards.default.menu import menu
from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await message.answer("Videolarni tanlang👇", reply_markup=menu)


@dp.message_handler(text="Messi - Edits")
async def show_menu(message: Message):
    await message.answer("Videolarni tanlang👇", reply_markup=menuMessi)


@dp.message_handler(text="Bosh menyuga")
async def show_menu(massage: Message):
    await massage.answer('Videolarni tanlang', reply_markup=menu)
