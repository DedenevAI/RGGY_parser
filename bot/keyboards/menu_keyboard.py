from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from text_holder.text_elements_enum import ButtonsName


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


def show_again() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=ButtonsName.again.value.capitalize())
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
