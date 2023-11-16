from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import enum


def menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="🎫Хочу узнать расписание!")
    kb.button(text="🖥Автор")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def choice_schedulle() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Расписание по потоку")
    kb.button(text="Расписание по преподователю")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def choice_graduate() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Дневная")
    kb.button(text="Вечерняя")
    kb.button(text="Заочная")
    kb.button(text="Второе высшее")
    kb.button(text="Магистратура")
    kb.button(text="Аспирантура")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def choice_kurs() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Курс 1")
    kb.button(text="Курс 2")
    kb.button(text="Курс 3")
    kb.button(text="Курс 4")
    kb.button(text="Курс 5")
    kb.button(text="Курс 6")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def choice_srok() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="На сегодня/завтра")
    kb.button(text="На неделю")
    kb.button(text="На месяц")
    kb.button(text="На семестр")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
