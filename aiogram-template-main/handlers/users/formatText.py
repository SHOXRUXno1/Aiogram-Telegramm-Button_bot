from aiogram import types

from loader import dp


@dp.message_handler(commands="info_html")
async def bot_help(msg: types.Message):
    text = f"Assalomu aleykum {msg.from_user.full_name}!\n"
    text += "Bu <b> qalin </b> shrift\n"
    text += "Bu <i> og'ma </i> shrift\n"
    text += "Bu <s> o'rta chiziq </s> shirft\n"
    text += ("Bu <u> underline </u> shirft\n")
    text += "Bu <a href='https://youtu.be/L7xolstrHxg?si=jAciPRDkgpzTGhC4'> KEROSENE - CRYSTAL CASTLES [ULTRA SLOWED + REVERB] - Phonki </a>\n"
    text += "Bu kod: <code> print('Salom') </code>"
    await msg.answer(text)
