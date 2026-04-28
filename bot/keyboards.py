from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="/cases"), KeyboardButton(text="/subscriptions")],
        ],
        resize_keyboard=True,
    )
