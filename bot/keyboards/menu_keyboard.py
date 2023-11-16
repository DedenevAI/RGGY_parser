from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import enum


class ButtonsName(enum.Enum):
    schedule_main = "хочу узнать расписание!🎫"
    author = "автор🖥"
    schedule = ["расписание по потоку", "расписание по преподователю"]
    graduate = {"Д": "дневная", "В": "вечерняя", "З": "заочная", "2": "второе высшее",
                "М": "магистратура", "А": "аспирантура", "У": "дистанционное"}
    kurs = {"1": "курс 1", "2": "курс 2", "3": "курс 3", "4": "курс 4",
            "5": "курс 5", "6": "курс 6"}
    srok = {"today": "на сегодня/завтра", "week": "на неделю", "month": "на месяц", "sem": "на семестр"}


def menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=ButtonsName.schedule_main.value.capitalize())
    kb.button(text=ButtonsName.author.value.capitalize())
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def choice_schedulle() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=ButtonsName.schedule.value[0].capitalize())
    kb.button(text=ButtonsName.schedule.value[1].capitalize())
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def choice_graduate() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=str(ButtonsName.graduate.value.get("Д")).capitalize())
    kb.button(text=str(ButtonsName.graduate.value.get("В")).capitalize())
    kb.button(text=str(ButtonsName.graduate.value.get("З")).capitalize())
    kb.button(text=str(ButtonsName.graduate.value.get("2")).capitalize())
    kb.button(text=str(ButtonsName.graduate.value.get("М")).capitalize())
    kb.button(text=str(ButtonsName.graduate.value.get("А")).capitalize())
    kb.button(text=str(ButtonsName.graduate.value.get("У")).capitalize())
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def choice_kurs() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=str(ButtonsName.kurs.value.get("1")).capitalize())
    kb.button(text=str(ButtonsName.kurs.value.get("2")).capitalize())
    kb.button(text=str(ButtonsName.kurs.value.get("3")).capitalize())
    kb.button(text=str(ButtonsName.kurs.value.get("4")).capitalize())
    kb.button(text=str(ButtonsName.kurs.value.get("5")).capitalize())
    kb.button(text=str(ButtonsName.kurs.value.get("6")).capitalize())
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def choice_srok() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=str(ButtonsName.srok.value.get("today")).capitalize())
    kb.button(text=str(ButtonsName.srok.value.get("week")).capitalize())
    kb.button(text=str(ButtonsName.srok.value.get("month")).capitalize())
    kb.button(text=str(ButtonsName.srok.value.get("sem")).capitalize())
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
