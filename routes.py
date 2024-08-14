from aiogram import F, types, Router
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext

from models import Form
from utils import word_request, escape_markdown_v2, make_row_keyboard, get_word, sentence_checker

router = Router()


@router.message(StateFilter(None), Command("start"))
async def send_welcome(message: types.Message):
    keyboard = make_row_keyboard(["/random_word", "/sentence"])
    await message.answer(f"Cooking???", reply_markup=keyboard)


@router.message(StateFilter(None), Command("random_word"))
async def random_word_responce(message: types.Message):
    answer = await word_request()
    keyboard = make_row_keyboard(["/random_word", "/sentence"])
    await message.reply(escape_markdown_v2(answer), reply_markup=keyboard, parse_mode='MarkdownV2')


@router.message(StateFilter(None), Command("sentence"))
async def create_sentences(message: types.Message, state: FSMContext):
    answer = "Составь предложения с этим словом:\n" + get_word()
    await state.set_state(Form.waiting_for_text)
    await message.reply(escape_markdown_v2(answer), parse_mode='MarkdownV2')


@router.message(Form.waiting_for_text)
async def get_sentence_from_user(message: types.Message, state: FSMContext):
    answer = await sentence_checker(message.text)
    await message.answer(escape_markdown_v2(answer), parse_mode='MarkdownV2')
    await state.clear()
