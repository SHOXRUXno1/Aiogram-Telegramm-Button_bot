from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.personalData import personalData


@dp.message_handler(Command('anketa'), state=None)
async def enter_test(meesage: types.Message):
    await meesage.answer("To'liq Ismingznii Kiriting")
    await personalData.fullname.set()


@dp.message_handler(state=personalData.fullname)
async def answer_fullname(meesage: types.Message, state: FSMContext):
    full_name = meesage.text
    await state.update_data(name=full_name)
    await state.update_data(
        {'name': full_name}
    )
    await meesage.answer("Emalingizni kiriting")
    await personalData.next()


@dp.message_handler(state=personalData.email)
async def answer_email(meesage: types.Message, state: FSMContext):
    email = meesage.text

    await state.update_data(
        {"email": email}
    )

    await meesage.answer("Telefon raqamingzni kiriting")

    await personalData.next()


@dp.message_handler(state=personalData.phoneNum)
async def answer_phone(meesage: types.Message, state: FSMContext):
    phone = meesage.text

    await state.update_data(
        {"phone": phone}
    )

    data = await state.get_data()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    msg = "Quydagi ma'lumoptlar qabil qilindi:\n"
    msg += f"Ismingiz - {name}\n"
    msg += f"Email - {email}\n"
    msg += f"Telefon raqamingiz - {phone}"

    await meesage.answer(msg)

    await state.finish()
