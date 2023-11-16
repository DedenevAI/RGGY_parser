from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import enum

class ButtonsName(enum.Enum):
    schedule_main = "🎫Хочу узнать расписание!"
    author = "🖥Автор"
    schedule = ["Расписание по потоку", "Расписание по преподователю"]
    graduate = {"Д" : "Дневная", "В" : "Вечерняя", "З" : "Заочная", "2":"2-ое высшее", 
                "М" : "Магистратура", "А" : "Аспирантура", "У" : "Дистанционное"}
    kurs = {"1" : "Курс 1", "2" : "Курс 2", "3" : "Курс 3", "4" :"Курс 4", 
                "5" : "Курс 5", "6" : "Курс 6"}
    srok = {"today" : "На сегодня/завтра", "week" : "На неделю", "month" : "На месяц", "sem" : "На семестр"}



def menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text = ButtonsName.schedule_main.value)
    kb.button(text = ButtonsName.author.value)
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def choice_schedulle() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text= ButtonsName.schedule.value[0])
    kb.button(text= ButtonsName.schedule.value[1])
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def choice_graduate() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=ButtonsName.graduate.value.get("Д"))
    kb.button(text=ButtonsName.graduate.value.get("В"))
    kb.button(text=ButtonsName.graduate.value.get("З"))
    kb.button(text=ButtonsName.graduate.value.get("2"))
    kb.button(text=ButtonsName.graduate.value.get("М"))
    kb.button(text=ButtonsName.graduate.value.get("А"))
    kb.button(text=ButtonsName.graduate.value.get("У"))
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def choice_kurs() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=ButtonsName.kurs.value.get("1"))
    kb.button(text=ButtonsName.kurs.value.get("2"))
    kb.button(text=ButtonsName.kurs.value.get("3"))
    kb.button(text=ButtonsName.kurs.value.get("4"))
    kb.button(text=ButtonsName.kurs.value.get("5"))
    kb.button(text=ButtonsName.kurs.value.get("6"))
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def choice_srok() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=ButtonsName.srok.value.get("today"))
    kb.button(text=ButtonsName.srok.value.get("week"))
    kb.button(text=ButtonsName.srok.value.get("month"))
    kb.button(text=ButtonsName.srok.value.get("sem"))
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
