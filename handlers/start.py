from aiogram import Router
from aiogram import F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, FSInputFile
from pdftoimage import rasp

start_router = Router()
def chooseclass(uclass):
    @start_router.message(uclass)
    async def cmd_start(message: Message):
        kb = [
            [KeyboardButton(text="/5А")],
            [KeyboardButton(text="/5Б")],
            [KeyboardButton(text="/6А")],
            [KeyboardButton(text="/6Б")],
            [KeyboardButton(text="/6В")],
            [KeyboardButton(text="/7А")],
            [KeyboardButton(text="/7Б")],
            [KeyboardButton(text="/7В")],
            [KeyboardButton(text="/8А")],
            [KeyboardButton(text="/8Б")],
            [KeyboardButton(text="/9А")],
            [KeyboardButton(text="/9Б")],
            [KeyboardButton(text="/10А")],
            [KeyboardButton(text="/10Б")],
            [KeyboardButton(text="/11А")],
            [KeyboardButton(text="/11Б")]
        ]
        keyboard = ReplyKeyboardMarkup(keyboard=kb)
        await message.answer("Выбери свой класс", reply_markup=keyboard)
def chooseday(urclass):
    @start_router.message(Command(f"{urclass}"))
    async def choose(message: Message):
        await message.answer("Спасибо за ответ!")
        kb = [
            [KeyboardButton(text=f"/Понедельник{urclass}")],
            [KeyboardButton(text=f"/Вторник{urclass}")],
            [KeyboardButton(text=f"/Среда{urclass}")],
            [KeyboardButton(text=f"/Четверг{urclass}")],
            [KeyboardButton(text=f"/Пятница{urclass}")],
            [KeyboardButton(text=f"/Суббота{urclass}")],
            [KeyboardButton(text=f"/Назад")],
        ]
        keyboard = ReplyKeyboardMarkup(keyboard=kb)
        await message.answer("Выбери день", reply_markup=keyboard)



def sendphoto(urclass1, Day):
    print(f"{Day} {urclass1}")
    @start_router.message(Command(f"{Day}{urclass1}"))
    async def upload_photo(message: Message):
        image_from_pc = FSInputFile(f".\image\{Day}{urclass1}.jpg")
        result = await message.answer_photo(
        image_from_pc,
        caption=f"{Day} {urclass1}"
    )
def oneclass(myclass):
    sendphoto(f"{myclass}", "Понедельник"), sendphoto(f"{myclass}", "Вторник"), sendphoto(f"{myclass}", "Среда"), sendphoto(f"{myclass}", "Четверг"), sendphoto(f"{myclass}", "Пятница"), sendphoto("5А", "Суббота")
