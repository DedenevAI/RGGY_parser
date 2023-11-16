from aiogram import Router, F
from aiogram import html
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile
from keyboards.menu_keyboard import menu, choice_schedulle, choice_graduate, choice_kurs, choice_srok, ButtonsName
from parser import parser_1
import time

router = Router()


class Status(StatesGroup):
    menu_activity = State()
    forming_information_for_parse = State()
    parsing = State()


@router.message(StateFilter(None), Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(
        f"👋Привет, {html.bold(html.quote(message.from_user.full_name))}! Я бот, который призван помочь тебе узнать "
        f"актуальное расписание пар! Пожалуйста, для дальнейшей работы воспользуйся кнопками меню.",
        reply_markup=menu()
    )
    await state.set_state(Status.menu_activity)


# showing the author's information
@router.message(Status.menu_activity, F.text.lower() == ButtonsName.author.value)
async def show_author(message: Message):
    await message.answer(
        ButtonsName.graduate.value.values() +
        "Студент группы ФИСБ_ПИ_ПИГС\nАлександр Деденев\nGitHub: https://github.com/DedenevAI/DedenevAI"
    )


# choosing the types of getting schedule
@router.message(Status.menu_activity,
                F.text.lower() == ButtonsName.schedule_main.value)
async def show_schedulle_types(message: Message, state: FSMContext):
    await message.answer(
        "Какое расписание ты хочешь просмотреть?",
        reply_markup=choice_schedulle()
    )
    await state.set_state(Status.forming_information_for_parse)


@router.message(Status.forming_information_for_parse,
                F.text.lower() == str(ButtonsName.schedule.value[0]).lower())
async def show_graduate(message: Message):
    await message.answer(
        "Выбери форму обучения:",
        reply_markup=choice_graduate()
    )


@router.message(Status.forming_information_for_parse,
                F.text.lower().in_(ButtonsName.graduate.value.values()))
async def show_kurs(message: Message, state: FSMContext):
    await state.update_data(formob=message.text.lower())
    await message.answer(
        "Выбери курс обучения:",
        reply_markup=choice_kurs()
    )


@router.message(Status.forming_information_for_parse,
                F.text.lower().in_(ButtonsName.kurs.value.values()))
async def show_srok(message: Message, state: FSMContext):
    await state.update_data(kurs=message.text.lower())
    await message.answer(
        "На какой период необходимо отобразить расписание?",
        reply_markup=choice_srok()
    )


@router.message(Status.forming_information_for_parse,
                F.text.lower().in_(ButtonsName.srok.value.values()))
async def show_srok(message: Message, state: FSMContext):
    await state.update_data(srok=message.text.lower())

    if (message.text.lower() == str(ButtonsName.srok.value.get("month")).lower() or
            message.text.lower() == str(ButtonsName.srok.value.get("sem")).lower()):
        await state.update_data(download_mode=1)
    else:
        await state.update_data(download_mode=0)

    await message.answer(
        "Введите, пожалуйста, название вашего потока:",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(Status.parsing)


@router.message(Status.parsing)
async def show_schedule(message: Message, state: FSMContext):
    await state.update_data(caf=message.text.lower())
    user_data = await state.get_data()

    download_mode = bool(user_data['download_mode'])
    formob = user_data['formob']
    kurs = user_data['kurs']
    srok = user_data['srok']
    caf = user_data['caf']

    await message.answer(
        "Расписание формируется, пожалуйста, подождите \n" +
        formob + " " + kurs + " " + srok + " " + caf + " " + str(download_mode)
    )

    if download_mode:
        
        parser_1.Potok_parser(formob, kurs, srok, caf, download_mode).parse()
        time.sleep(20)

        schedule = FSInputFile("/Users/alexded/Desktop/rg_sch_par/bot/files/schedule.xlsx")

        await message.answer_document(
            schedule,
            caption="Расписание:"
        )
    else:

        table = parser_1.Potok_parser(formob, kurs, srok, caf, download_mode).parse()

        await message.answer(
            f"{table}", parse_mode=ParseMode.HTML
        )
    await state.clear()
