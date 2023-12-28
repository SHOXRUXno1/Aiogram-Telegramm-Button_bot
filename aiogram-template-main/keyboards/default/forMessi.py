from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuMessi = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text="1video"),
        ],
        [
            KeyboardButton(text="2video"),
        ],
        [
            KeyboardButton(text="3video")
        ],
        [
            KeyboardButton(text="Bosh menyuga"),
        ],
    ],
    resize_keyboard=True
)
