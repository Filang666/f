from start import chooseday, oneclass, chooseclass
from aiogram.filters import CommandStart, Command

chooseclass(CommandStart())

chooseday("5А"), chooseday("5Б"), chooseday("6А"), chooseday("6Б"), chooseday("6В"), chooseday("7А"), chooseday("7Б"), chooseday("7В")
chooseday("8А"), chooseday("8Б"), chooseday("9А"), chooseday("9Б"), chooseday("10А"), chooseday("10Б"), chooseday("11А"), chooseday("11Б")

chooseclass(Command("Назад"))

oneclass("5А"), oneclass("5Б"), oneclass("6А"), oneclass("6Б"), oneclass("6В"), oneclass("7А"), oneclass("7Б"), oneclass("7В")
oneclass("8А"), oneclass("8Б"), oneclass("9А"), oneclass("9Б"), oneclass("10А"), oneclass("10Б"), oneclass("11А"), oneclass("11Б")