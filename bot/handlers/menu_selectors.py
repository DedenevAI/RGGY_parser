import time
import os
from aiogram import Router, F
from aiogram import html
from aiogram.enums import ParseMode
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import FSInputFile
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.menu_keyboard import menu, choice_schedulle, choice_graduate, choice_kurs, choice_srok, show_again
from parser import schedule_parser
from text_holder.text_elements_enum import ButtonsName, BotMessage

router = Router()


class Status(StatesGroup):
    menu_activity = State()
    forming_information_for_parse_group = State()
    forming_information_for_parse_teach = State()
    parsing = State()


@router.message(StateFilter(None), Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(
        f"👋Привет, {html.bold(html.quote(message.from_user.full_name))}! Я бот, который призван помочь тебе узнать "
        f"актуальное расписание пар! Пожалуйста, для дальнейшей работы воспользуйся кнопками меню.",
        reply_markup=menu()
    )
    await state.set_state(Status.menu_activity)

    @router.message(Status.menu_activity or Status.forming_information_for_parse_group or Status.parsing, F.text)
    async def for_spam(message: Message):
        await message.answer(
            BotMessage.menu_warning.value
        )


# showing the author's information
@router.message(Status.menu_activity, F.text.lower() == ButtonsName.author.value)
async def show_author(message: Message):
    await message.answer(
        BotMessage.author_information.value
    )


# choosing the types of getting schedule
@router.message(Command(commands=["return"]))
@router.message(Status.menu_activity,
                F.text.lower() == ButtonsName.schedule_main.value or F.text.lower() == str(
                    ButtonsName.again.value).lower())
async def show_schedulle_types(message: Message, state: FSMContext):
    await message.answer(
        BotMessage.show_schedulle.value,
        reply_markup=choice_schedulle()
    )


@router.message(Status.menu_activity,
                F.text.lower() == str(ButtonsName.schedule.value[1]).lower())
async def show_teacher_writer(message: Message, state: FSMContext):
    await state.update_data(parse_mode="teach")
    await message.answer(
        BotMessage.show_teacher_writer.value,
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(Status.forming_information_for_parse_teach)


@router.message(Status.menu_activity,
                F.text.lower() == str(ButtonsName.schedule.value[0]).lower())
async def show_graduate(message: Message, state: FSMContext):
    await state.update_data(parse_mode="group")
    await message.answer(
        BotMessage.show_graduate.value,
        reply_markup=choice_graduate()
    )
    await state.set_state(Status.forming_information_for_parse_group)


@router.message(Status.forming_information_for_parse_group,
                F.text.lower().in_(ButtonsName.graduate.value.values()))
async def show_kurs(message: Message, state: FSMContext):
    await state.update_data(formob=message.text.lower())
    await message.answer(
        BotMessage.show_kurs.value,
        reply_markup=choice_kurs()
    )


@router.message(Status.forming_information_for_parse_group, F.text.lower().in_(ButtonsName.kurs.value.values()))
async def show_srok_for_group(message: Message, state: FSMContext):
    await state.update_data(kurs=message.text.lower())
    await message.answer(
        BotMessage.show_srok.value,
        reply_markup=choice_srok()
        )


@router.message(Status.forming_information_for_parse_teach, F.text)
async def show_srok_for_teach(message: Message, state: FSMContext):
    await state.update_data(kurs=message.text.lower())
    await message.answer(
        BotMessage.show_srok.value,
        reply_markup=choice_srok()
        )
    await state.set_state(Status.parsing)


@router.message(Status.forming_information_for_parse_group,
                F.text.lower().in_(ButtonsName.srok.value.values()))
async def show_group_writer(message: Message, state: FSMContext):
    await state.update_data(srok=message.text.lower())
    await state.update_data(download_mode=download_mode_set(message.text.lower()))

    await message.answer(
        BotMessage.show_group_writer.value,
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(Status.parsing)


@router.message(Status.parsing)
async def show_schedule(message: Message, state: FSMContext):
    await state.update_data(input_data=message.text.lower())

    if message.text.lower() in ButtonsName.srok.value.values():
        await state.update_data(download_mode=download_mode_set(message.text.lower()))

    user_data = await state.get_data()

    parse_mode = user_data['parse_mode']
    download_mode = bool(user_data['download_mode'])

    await message.answer(
        BotMessage.please_wait.value
    )

    if parse_mode == 'group':
        formob = user_data['formob']
        kurs = user_data['kurs']
        srok = user_data['srok']
        input_data = user_data['input_data']

        parser = (schedule_parser.ParserUni(srok, input_data, download_mode, parse_mode, formob=formob, kurs=kurs)
                  .parse_group())

    else:
        srok = user_data['input_data']
        input_data = user_data['kurs']

        parser = schedule_parser.ParserUni(srok, input_data, download_mode, parse_mode).parse_teacher()

    if parser == 0:
        await message.answer(
            BotMessage.warning.value,
            reply_markup=show_again()
        )

    elif download_mode:
        time.sleep(20)

        schedule = FSInputFile("/Users/alexded/Desktop/rg_sch_par/bot/files/schedule.xlsx")

        await message.answer_document(
            schedule,
            caption="Расписание:",
            reply_markup=show_again()
        )
        os.remove("/Users/alexded/Desktop/rg_sch_par/bot/files/schedule.xlsx")
    else:
        await message.answer(
            f"{parser}", parse_mode=ParseMode.HTML,
            reply_markup=show_again()
        )
    await state.clear()
    await state.set_state(Status.menu_activity)


def download_mode_set(string):
    if (string == str(ButtonsName.srok.value.get("month")).lower() or
            string == str(ButtonsName.srok.value.get("sem")).lower()):
        return 1
    else:
        return 0
