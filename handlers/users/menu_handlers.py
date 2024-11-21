from aiogram import types
from loader import dp,bot
from keyboards.inline.start_menu import menu,course_menu

@dp.callback_query_handler(text='about')
async def about_message(call:types.CallbackQuery):
    text="IT TAT o`quv markazi zamonaviy IT yo`nalishlatda ta`lim beradi\n"
    text+="Maqsadimiz - yoshalarni zamonaviy bilimlar bilan ta`limlashw\n\n"
    await call.message.edit_text(text,reply_markup=menu,parse_mode="Markdown")
    await call.answer()




@dp.callback_query_handler(text='news')
async def about_message(call:types.CallbackQuery):
    text="Hozir bizda aksiya bir o`qisang bir oy tekin o`qiysan \n"
    text+="bizda 32-octabr kuni olimpiyada \n\n"
    await call.message.edit_text(text,parse_mode="Markdown")
    await call.answer()


@dp.callback_query_handler(text='news')
async def about_message(call:types.CallbackQuery):
    text="telefon raqamingiz +50 002 36 88"
    await call.message.edit_text(text,parse_mode="Markdown")
    await call.answer()

@dp.callback_query_handler(text='courses')
async def about_message(call:types.CallbackQuery):
    text="Bizda mavjud kursalar\n\n"
    await call.message.edit_text(text,reply_markup=course_menu,parse_mode="Markdown")
    await call.answer()

































