from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.start_menu import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text=f"Salom, {message.from_user.full_name}!"
    text+=f"Sizni bugun IT TAT O`quv markazida ko`rib turganimizdan xursanmiz😘\n\n"
    text+=f"Biznig bot orqali:\n"
    text+=f" - MAvjudkurslar bilan tanishishingiz\n"
    text+=f" - Kurslardan ro`yxatdan o`tishingiz\n"
    text+=f" - yangiliklardan xabardor bo`lishingiz \n"
    text+=f"boshlash uchun tugmalardan biri  tanlang va boz haqimixda ma`lumot oling."
    await message.answer(text,reply_markup=menu,parse_mode="Markdown")
