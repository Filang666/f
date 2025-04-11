from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    kb = [
        [KeyboardButton(text="5А")],
        [KeyboardButton(text="5Б")],
        [KeyboardButton(text="6А")],
        [KeyboardButton(text="6Б")],
        [KeyboardButton(text="6В")],
        [KeyboardButton(text="7А")],
        [KeyboardButton(text="7Б")],
        [KeyboardButton(text="7В")],
        [KeyboardButton(text="8А")],
        [KeyboardButton(text="8Б")],
        [KeyboardButton(text="9А")],
        [KeyboardButton(text="9Б")],
        [KeyboardButton(text="10А")],
        [KeyboardButton(text="10Б")],
        [KeyboardButton(text="11А")],
        [KeyboardButton(text="11Б")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Выбери свой класс", reply_markup=keyboard)
