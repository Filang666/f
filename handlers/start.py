from aiogram import Router
from aiogram import F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, FSInputFile


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
sendphoto("5А", "Понедельник"), sendphoto("5А", "Вторник"), sendphoto("5А", "Среда"), sendphoto("5А", "Четверг"), sendphoto("5А", "Пятница"), sendphoto("5А", "Суббота")
sendphoto("5Б", "Понедельник"), sendphoto("5Б", "Вторник"), sendphoto("5Б", "Среда"), sendphoto("5Б", "Четверг"), sendphoto("5Б", "Пятница"), sendphoto("5Б", "Суббота")
sendphoto("6А", "Понедельник"), sendphoto("6А", "Вторник"), sendphoto("6А", "Среда"), sendphoto("6А", "Четверг"), sendphoto("6А", "Пятница"), sendphoto("6А", "Суббота")
sendphoto("6Б", "Понедельник"), sendphoto("6Б", "Вторник"), sendphoto("6Б", "Среда"), sendphoto("6Б", "Четверг"), sendphoto("6Б", "Пятница"), sendphoto("6Б", "Суббота")
sendphoto("6В", "Понедельник"), sendphoto("6В", "Вторник"), sendphoto("6В", "Среда"), sendphoto("6В", "Четверг"), sendphoto("6В", "Пятница"), sendphoto("6В", "Суббота")
sendphoto("7А", "Понедельник"), sendphoto("7А", "Вторник"), sendphoto("7А", "Среда"), sendphoto("7А", "Четверг"), sendphoto("7А", "Пятница"), sendphoto("7А", "Суббота")
sendphoto("7Б", "Понедельник"), sendphoto("7Б", "Вторник"), sendphoto("7Б", "Среда"), sendphoto("7Б", "Четверг"), sendphoto("7Б", "Пятница"), sendphoto("7Б", "Суббота")
sendphoto("7В", "Понедельник"), sendphoto("7В", "Вторник"), sendphoto("7В", "Среда"), sendphoto("7В", "Четверг"), sendphoto("7В", "Пятница"), sendphoto("7В", "Суббота")
sendphoto("8А", "Понедельник"), sendphoto("8А", "Вторник"), sendphoto("8А", "Среда"), sendphoto("8А", "Четверг"), sendphoto("8А", "Пятница"), sendphoto("8А", "Суббота")
sendphoto("8Б", "Понедельник"), sendphoto("8Б", "Вторник"), sendphoto("8Б", "Среда"), sendphoto("8Б", "Четверг"), sendphoto("8Б", "Пятница"), sendphoto("8Б", "Суббота")
sendphoto("9А", "Понедельник"), sendphoto("9А", "Вторник"), sendphoto("9А", "Среда"), sendphoto("9А", "Четверг"), sendphoto("9А", "Пятница"), sendphoto("9А", "Суббота")
sendphoto("9Б", "Понедельник"), sendphoto("9Б", "Вторник"), sendphoto("9Б", "Среда"), sendphoto("9Б", "Четверг"), sendphoto("9Б", "Пятница"), sendphoto("9Б", "Суббота")
sendphoto("10А", "Понедельник"), sendphoto("10А", "Вторник"), sendphoto("10А", "Среда"), sendphoto("10А", "Четверг"), sendphoto("10А", "Пятница"), sendphoto("10А", "Суббота")
sendphoto("10Б", "Понедельник"), sendphoto("10Б", "Вторник"), sendphoto("10Б", "Среда"), sendphoto("10Б", "Четверг"), sendphoto("10Б", "Пятница"), sendphoto("10Б", "Суббота")
sendphoto("11А", "Понедельник"), sendphoto("11А", "Вторник"), sendphoto("11А", "Среда"), sendphoto("11А", "Четверг"), sendphoto("11А", "Пятница"), sendphoto("11А", "Суббота")
sendphoto("11Б", "Понедельник"), sendphoto("11Б", "Вторник"), sendphoto("11Б", "Среда"), sendphoto("11Б", "Четверг"), sendphoto("11Б", "Пятница"), sendphoto("11Б", "Суббота")


@start_router.message(Command("скиньхуй"))
async def sendhui(message: Message):
    if message.from_user.id in (1193425859, 5191099515):
        await message.answer_photo(FSInputFile(f".\hui.jpg"))
    else:
        await message.answer("Пошел нахуй!")
        print(message.from_user.id)
