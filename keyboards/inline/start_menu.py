from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup



menu=InlineKeyboardMarkup(
    inline_keyboard=

[

    [


        InlineKeyboardButton(text="📚maxjud Kurslar",callback_data='courses'),
        InlineKeyboardButton(text="ℹ️biz haqimizda",callback_data='about'),
    ],
    [
        InlineKeyboardButton(text="📞Aloqa", callback_data='contact'),
        InlineKeyboardButton(text="🏘️Manzil", callback_data='location'),

    ],
    [
        InlineKeyboardButton(text="📑Ro`y xatdan utish", callback_data='register'),
        InlineKeyboardButton(text="🆕Yangiliklar", callback_data='news'),
    ],
    [
        InlineKeyboardButton(text="takliflar", callback_data='feedback'),
    ],





],


)

course_menu=InlineKeyboardMarkup(
    inline_keyboard=

[

    [


        InlineKeyboardButton(text="📚backend",callback_data='backend'),
        InlineKeyboardButton(text="ℹ️fronted",callback_data='frontend'),
    ],
    [
        InlineKeyboardButton(text="📞SMM", callback_data='SMM'),
        InlineKeyboardButton(text="🏘ROBOT", callback_data='BOSSBOT'),

    ],
    [
        InlineKeyboardButton(text="📑kompyuter savondxonligi", callback_data='kompyuter'),
        InlineKeyboardButton(text="🆕darkned", callback_data='dark_net'),
    ],
    [
        InlineKeyboardButton(text="Orqa", callback_data='Back'),
    ],





],


)

