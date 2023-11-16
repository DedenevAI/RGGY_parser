from aiogram import Router, F
from aiogram import html
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile
import sys
import time
sys.path.append("/Users/alexded/Desktop/rg_sch_par/bot/parser")
sys.path.append("/Users/alexded/Desktop/rg_sch_par/bot/keyboards")

from keyboards.menu_keyboard import menu, choice_schedulle, choice_graduate, choice_kurs, choice_srok
from parser import parser_1

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"👋Привет, {html.bold(html.quote(message.from_user.full_name))}! Я бот, который призван помочь тебе узнать актуальное расписание пар! Пожалуйста, для дальнейшей работы воспользуйся кнопками меню.",
        reply_markup=menu()
    )


# showing the author's information
@router.message(F.text.lower() == "🖥автор")
async def show_author(message: Message):
    await message.answer(
        "Студент группы ФИСБ_ПИ_ПИГС\nАлександр Деденев\nGitHub: https://github.com/DedenevAI/DedenevAI"
    )


# choosing the various of getting schedulle
@router.message(F.text.lower() == "🎫хочу узнать расписание!")
async def show_schedulle_types(message: Message):
    await message.answer(
        "Какое расписание ты хочешь просмотреть?",
        reply_markup=choice_schedulle()
    )


@router.message(F.text.lower() == "расписание по потоку")
async def show_graduate(message: Message):
    await message.answer(
        "Выбери форму обучения:",
        reply_markup=choice_graduate()
    )


@router.message(F.text.lower().in_({"дневная", "вечерняя", "заочная", "второе высшее", "магистратура", "аспирантура"}))
async def show_kurs(message: Message):
    global formob1
    formob1 = message.text
    await message.answer(
        "Выбери курс обучения:",
        reply_markup=choice_kurs()
    )


@router.message(F.text.lower().in_({"курс 1", "курс 2", "курс 3", "курс 4", "курс 5", "курс 6"}))
async def show_srok(message: Message):
    global kurs
    kurs = message.text
    await message.answer(
        "На какой период необходимо отобразить расписание?",
        reply_markup=choice_srok()
    )


@router.message(F.text.lower().in_({"на сегодня/завтра", "на неделю", "на месяц", "на семестр"}))
async def show_srok(message: Message):
    global srok, download_mode
    download_mode = False
    srok = message.text
    if srok.lower() == "на месяц" or "на семестр":
        download_mode = True
    await message.answer(
        "Введите, пожалуйста, название вашего потока:",
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(F.text)
async def show_schedule(message: Message):
    global caf
    caf = message.text

    if download_mode == False:
        table = parser_1.Potok_parser(formob1, kurs, srok, caf, download_mode).parse()
        await message.answer(
            f"{table}", parse_mode = ParseMode.HTML
        )
    else:
        await message.answer(
            "Идет подготовка файла, пожалуйста, подождите..."
        )
        parser_1.Potok_parser(formob1, kurs, srok, caf, download_mode).parse()
        time.sleep(20)

        schedule = FSInputFile("/Users/alexded/Desktop/rg_sch_par/bot/files/schedule.xlsx")
        await message.answer_document(
            schedule,
            caption= "Расписание:"
        )

