"""
EduBot - Telegram Ta'lim Bot va WebApp serveri
Ushbu bot Telegram foydalanuvchilariga O'quv platformasini WebApp shaklida taqdim etadi.

O'rnatish:
    pip install aiogram

Ishga tushirish:
    python bot.py
"""

import os
import json
import logging
import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
    MenuButtonWebApp
)

# 1. Sozlamalar (Token va WebApp URL)
BOT_TOKEN = os.getenv("BOT_TOKEN", "BOT_TOKENINGIZNI_BU_YERGA_YOZING")

# Netlify-da deploy qilingan sayt URL manzili (yoki o'zingizning domeningiz)
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://edubot-platform.netlify.app")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# 2. /start komandasi
@dp.message(CommandStart())
async def handle_start(message: types.Message):
    user_name = message.from_user.first_name

    # Bot menyu tugmasini WebApp sifatida sozlash
    try:
        await bot.set_chat_menu_button(
            chat_id=message.chat.id,
            menu_button=MenuButtonWebApp(
                text="🎓 Platforma",
                web_app=WebAppInfo(url=WEBAPP_URL)
            )
        )
    except Exception as e:
        logging.warning(f"Menyu tugmasini sozlashda xatolik: {e}")

    # Chiroyli klaviatura
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🚀 O'quv Platformasini Ochish",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ],
            [
                InlineKeyboardButton(text="📚 Barcha Kurslar", callback_data="show_courses"),
                InlineKeyboardButton(text="🏆 Yutuqlarim", callback_data="show_achievements")
            ],
            [
                InlineKeyboardButton(text="💬 Qo'llab-quvvatlash", url="https://t.me/telegram")
            ]
        ]
    )

    text = (
        f"Assalomu alaykum, <b>{user_name}</b>! 👋\n\n"
        f"<b>EduPlatform</b> – Zamonaviy IT va zamonaviy kasblar o'quv platformasiga xush kelibsiz!\n\n"
        f"🔹 <i>Dasturlash (Python, React, Django)</i>\n"
        f"🔹 <i>Sun'iy Intellekt va Prompt muhandisligi</i>\n"
        f"🔹 <i>Telegram Botlar yaratish</i>\n"
        f"🔹 <i>UI/UX Dizayn va Ingliz tili</i>\n\n"
        f"Platformadan to'liq foydalanish va darslarni boshlash uchun quyidagi tugmani bosing:"
    )

    await message.answer(text, reply_markup=keyboard, parse_mode="HTML")


# 3. /courses komandasi
@dp.message(Command("courses"))
async def handle_courses(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🌐 Kurslar Katalogini Ko'rish",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ]
        ]
    )
    await message.answer(
        "📖 <b>Mavjud O'quv Kurslari:</b>\n\n"
        "1. Telegram Botlar Yaratish (Aiogram 3)\n"
        "2. Zamonaviy Frontend & React\n"
        "3. Python Dasturlash & Django Backend\n"
        "4. Sun'iy Intellekt & Prompt Engineering\n"
        "5. UI/UX Dizayn & Figma\n"
        "6. IT uchun Ingliz Tili\n\n"
        "Kurs darslarini ko'rish uchun WebApp-ni oching:",
        reply_markup=keyboard,
        parse_mode="HTML"
    )


# 4. WebApp-dan kelgan ma'lumotlarni qabul qilish
@dp.message(F.web_app_data)
async def handle_webapp_data(message: types.Message):
    try:
        raw_data = message.web_app_data.data
        data = json.loads(raw_data)
        action = data.get("action")

        if action == "quiz_completed":
            course_title = data.get("course_title", "Kurs")
            score = data.get("score", 0)
            total = data.get("total", 0)
            percent = round((score / total) * 100) if total > 0 else 0

            response_text = (
                f"🎉 <b>Tabriklaymiz! Test yakunlandi!</b>\n\n"
                f"📌 <b>Kurs:</b> {course_title}\n"
                f"📊 <b>Natija:</b> {score} / {total} ball ({percent}%)\n\n"
            )
            if percent >= 70:
                response_text += "⭐️ Siz sertifikat talablariga muvaffaqiyatli javob berdingiz!"
            else:
                response_text += "💡 Natijangizni oshirish uchun darslarni yana bir bor ko'rib chiqishingiz mumkin."

            await message.answer(response_text, parse_mode="HTML")

        elif action == "enroll":
            course_id = data.get("course_id")
            await message.answer(
                f"✅ Siz <b>{course_id}</b> kursi uchun muvaffaqiyatli ro'yxatdan o'tdingiz!\n"
                "Darslarni istalgan vaqtda WebApp orqali davom ettirishingiz mumkin.",
                parse_mode="HTML"
            )
        else:
            await message.answer(f"Qabul qilindi: {data}")

    except Exception as e:
        logging.error(f"WebApp ma'lumotlarini o'qishda xatolik: {e}")
        await message.answer("Ma'lumotlar qabul qilindi!")


# 5. Callback so'rovlari
@dp.callback_query(F.data == "show_courses")
async def cb_courses(callback: types.CallbackQuery):
    await callback.message.answer(
        "Platformada 6+ ta amaliy kurslar mavjud! Quyidagi havola orqali kiring:",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(text="🎓 WebApp-ga Kirish", web_app=WebAppInfo(url=WEBAPP_URL))
            ]]
        )
    )
    await callback.answer()


@dp.callback_query(F.data == "show_achievements")
async def cb_achievements(callback: types.CallbackQuery):
    await callback.message.answer(
        "🏆 <b>Sizning Yutuqlaringiz:</b>\n\n"
        "• Faol o'quvchi nishoni 🎖\n"
        "• Ro'yxatdan o'tganlik uchun 10 ball ⭐\n\n"
        "Batafsil ma'lumot platformaning 'Profil' bo'limida aks etadi.",
        parse_mode="HTML"
    )
    await callback.answer()


async def main():
    if BOT_TOKEN == "BOT_TOKENINGIZNI_BU_YERGA_YOZING":
        print("\n⚠️ DIQQAT: bot.py faylidagi BOT_TOKEN o'zgaruvchisiga @BotFather dan olingan bot tokenini kiriting!\n")
    print("EduBot Telegram Bot ishga tushmoqda...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
