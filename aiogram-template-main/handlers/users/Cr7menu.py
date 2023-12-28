from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from keyboards.default.forCr7 import menuCr7, menuCr71, menuCr72
from keyboards.default.menu import menu
from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await message.answer("Videolarni tanlang👇", reply_markup=menu)


@dp.message_handler(text='Cr7 - Edits')
async def show_menu(message: Message):
    await message.answer("Darsni tanlang👇", reply_markup=menuCr7)


@dp.message_handler(text="Bosh menyuga")
async def show_menu(massage: Message):
    await massage.answer('Videolarni tanlang', reply_markup=menu)


@dp.message_handler(text='Oldinga')
async def show_menu(massage: Message):
    await massage.answer("Vidolarni Tanlang 👇", reply_markup=menuCr71)


@dp.message_handler(text='Ortga')
async def show_menu(massage: Message):
    await massage.answer("Vidolarni Tanlang 👇", reply_markup=menuCr7)


@dp.message_handler(text='Keyngisi')
async def show_menu(massage: Message):
    await massage.answer("Vidolarni Tanlang 👇", reply_markup=menuCr72)


@dp.message_handler(text='◀Ortga')
async def show_menu(massage: Message):
    await massage.answer("Vidolarni Tanlang 👇", reply_markup=menuCr71)
