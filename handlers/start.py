from aiogram import Router
from aiogram import F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, FSInputFile
from pdftoimage import rasp

start_router = Router()
@start_router.message(CommandStart())
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

chooseday("5А"), chooseday("5Б"), chooseday("6А"), chooseday("6Б"), chooseday("6В"), chooseday("7А"), chooseday("7Б"), chooseday("7В")
chooseday("8А"), chooseday("8Б"), chooseday("9А"), chooseday("9Б"), chooseday("10А"), chooseday("10Б"), chooseday("11А"), chooseday("11Б")

@start_router.message(Command("Назад"))
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

def sendphoto(urclass1, Day):
    print(f"{Day} {urclass1}")
    @start_router.message(Command(f"{Day}{urclass1}"))
    async def upload_photo(message: Message):
        image_from_pc = FSInputFile(f".\image\{Day}{urclass1}.jpg")
        result = await message.answer_photo(
        image_from_pc,
        caption=f"{Day} {urclass1}"
    )
sendphoto("5Аd", "Понедельник"), sendphoto("5Аd", "Вторник"), sendphoto("5Аd", "Среда"), sendphoto("5Аd", "Четверг"), sendphoto("5Аd", "Пятница"), sendphoto("5Аd", "Суббота")
sendphoto("5Бd", "Понедельник"), sendphoto("5Бd", "Вторник"), sendphoto("5Бd", "Среда"), sendphoto("5Бd", "Четверг"), sendphoto("5Бd", "Пятница"), sendphoto("5Бd", "Суббота")
sendphoto("6Аd", "Понедельник"), sendphoto("6Аd", "Вторник"), sendphoto("6Аd", "Среда"), sendphoto("6Аd", "Четверг"), sendphoto("6Аd", "Пятница"), sendphoto("6Аd", "Суббота")
sendphoto("6Бd", "Понедельник"), sendphoto("6Бd", "Вторник"), sendphoto("6Бd", "Среда"), sendphoto("6Бd", "Четверг"), sendphoto("6Бd", "Пятница"), sendphoto("6Бd", "Суббота")
sendphoto("6Вd", "Понедельник"), sendphoto("6Вd", "Вторник"), sendphoto("6Вd", "Среда"), sendphoto("6Вd", "Четверг"), sendphoto("6Вd", "Пятница"), sendphoto("6Вd", "Суббота")
sendphoto("7Аd", "Понедельник"), sendphoto("7Аd", "Вторник"), sendphoto("7Аd", "Среда"), sendphoto("7Аd", "Четверг"), sendphoto("7Аd", "Пятница"), sendphoto("7Аd", "Суббота")
sendphoto("7Бd", "Понедельник"), sendphoto("7Бd", "Вторник"), sendphoto("7Бd", "Среда"), sendphoto("7Бd", "Четверг"), sendphoto("7Бd", "Пятница"), sendphoto("7Бd", "Суббота")
sendphoto("7Вd", "Понедельник"), sendphoto("7Вd", "Вторник"), sendphoto("7Вd", "Среда"), sendphoto("7Вd", "Четверг"), sendphoto("7Вd", "Пятница"), sendphoto("7Вd", "Суббота")
sendphoto("8Аd", "Понедельник"), sendphoto("8Аd", "Вторник"), sendphoto("8Аd", "Среда"), sendphoto("8Аd", "Четверг"), sendphoto("8Аd", "Пятница"), sendphoto("8Аd", "Суббота")
sendphoto("8Бd", "Понедельник"), sendphoto("8Бd", "Вторник"), sendphoto("8Бd", "Среда"), sendphoto("8Бd", "Четверг"), sendphoto("8Бd", "Пятница"), sendphoto("8Бd", "Суббота")
sendphoto("9Аd", "Понедельник"), sendphoto("9Аd", "Вторник"), sendphoto("9Аd", "Среда"), sendphoto("9Аd", "Четверг"), sendphoto("9Аd", "Пятница"), sendphoto("9Аd", "Суббота")
sendphoto("9Бd", "Понедельник"), sendphoto("9Бd", "Вторник"), sendphoto("9Бd", "Среда"), sendphoto("9Бd", "Четверг"), sendphoto("9Бd", "Пятница"), sendphoto("9Бd", "Суббота")
sendphoto("10А", "Понедельник"), sendphoto("10А", "Вторник"), sendphoto("10А", "Среда"), sendphoto("10А", "Четверг"), sendphoto("10А", "Пятница"), sendphoto("10А", "Суббота")
sendphoto("10Б", "Понедельник"), sendphoto("10Б", "Вторник"), sendphoto("10Б", "Среда"), sendphoto("10Б", "Четверг"), sendphoto("10Б", "Пятница"), sendphoto("10Б", "Суббота")
sendphoto("11А", "Понедельник"), sendphoto("11А", "Вторник"), sendphoto("11А", "Среда"), sendphoto("11А", "Четверг"), sendphoto("11А", "Пятница"), sendphoto("11А", "Суббота")
sendphoto("11Б", "Понедельник"), sendphoto("11Б", "Вторник"), sendphoto("11Б", "Среда"), sendphoto("11Б", "Четверг"), sendphoto("11Б", "Пятница"), sendphoto("11Б", "Суббота")