"""
EduBot - Telegram Ta'lim Boti va WebApp Serveri
Muallif: d3000871-ui

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

# 1. Sozlamalar (Bot Token va WebApp URL)
BOT_TOKEN = os.getenv("BOT_TOKEN", "9201806873:AAELTm5p88mK9yNIfMUHB9cI7yQLFnnjY4s")

# Netlify yoki Render-dagi saytingiz havolasi
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://edubot-platform.onrender.com")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("EduBot")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def get_main_keyboard(url: str):
    """Asosiy WebApp tugmalari bilan klaviatura"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🚀 O'quv Platformasini Ochish",
                    web_app=WebAppInfo(url=url)
                )
            ],
            [
                InlineKeyboardButton(text="📚 Kurslar Katalogi", callback_data="show_courses"),
                InlineKeyboardButton(text="🏆 Yutuqlarim", callback_data="show_achievements")
            ],
            [
                InlineKeyboardButton(text="ℹ️ Bot haqida", callback_data="show_info"),
                InlineKeyboardButton(text="🌐 Saytga o'tish", url=url)
            ]
        ]
    )


# 2. /start buyrug'i
@dp.message(CommandStart())
async def handle_start(message: types.Message):
    global WEBAPP_URL
    user_name = message.from_user.first_name

    # Telegram chap pastki qismidagi "🎓 Platforma" menyu tugmasini ulash
    try:
        await bot.set_chat_menu_button(
            chat_id=message.chat.id,
            menu_button=MenuButtonWebApp(
                text="🎓 Platforma",
                web_app=WebAppInfo(url=WEBAPP_URL)
            )
        )
    except Exception as e:
        logger.warning(f"Menyu tugmasini sozlashda xatolik: {e}")

    text = (
        f"Assalomu alaykum, hurmatli <b>{user_name}</b>! 👋\n\n"
        f"🎓 <b>EduPlatform</b> – Zamonaviy IT va kasblar bo'yicha interaktiv o'quv platformasiga xush kelibsiz!\n\n"
        f"Platformamizda siz quyidagilarni o'rganishingiz mumkin:\n"
        f"🔹 <i>Python Dasturlash va Django Backend</i>\n"
        f"🔹 <i>Telegram Botlar Yaratish (Aiogram 3)</i>\n"
        f"🔹 <i>Zamonaviy Frontend (HTML, CSS, React)</i>\n"
        f"🔹 <i>Sun'iy Intellekt (AI) & Prompt muhandisligi</i>\n"
        f"🔹 <i>UI/UX Dizayn & Figma prototiplash</i>\n"
        f"🔹 <i>IT Sohasi uchun Ingliz Tili</i>\n\n"
        f"Darslarni boshlash, videolarni ko'rish va testlarni topshirish uchun quyidagi tugmani bosing:"
    )

    await message.answer(
        text,
        reply_markup=get_main_keyboard(WEBAPP_URL),
        parse_mode="HTML"
    )


# 3. /courses buyrug'i
@dp.message(Command("courses"))
async def handle_courses(message: types.Message):
    text = (
        "📖 <b>Mavjud O'quv Kurslari:</b>\n\n"
        "1. 🐍 <b>Python Backend & Django</b> - Noldan API yaratishgacha (28 dars)\n"
        "2. 🤖 <b>Telegram Botlar (Aiogram)</b> - Mini App va to'lov botlari (14 dars)\n"
        "3. 🌐 <b>Zamonaviy Frontend & React</b> - Interaktiv veb-saytlar (22 dars)\n"
        "4. 🧠 <b>AI & Prompt Engineering</b> - ChatGPT va Gemini sirlari (16 dars)\n"
        "5. 🎨 <b>UI/UX Dizayn & Figma</b> - Professional interfeys dizayni (18 dars)\n"
        "6. 🇬🇧 <b>IT uchun Ingliz Tili</b> - Texnik suhbatlardan o'tish (20 dars)\n\n"
        "Kurslar ichiga kirish va darslarni boshlash uchun quyidagi tugmani bosing:"
    )
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text="🎓 Kurslarni Ko'rish", web_app=WebAppInfo(url=WEBAPP_URL))
        ]]
    )
    await message.answer(text, reply_markup=kb, parse_mode="HTML")


# 4. /seturl buyrug'i (Admin uchun yangi WebApp URL sozlash)
@dp.message(Command("seturl"))
async def handle_seturl(message: types.Message):
    global WEBAPP_URL
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await message.answer(
            f"Hozirgi WebApp manzili:\n<code>{WEBAPP_URL}</code>\n\n"
            f"O'zgartirish uchun: <code>/seturl https://sizning-saytingiz.onrender.com</code>",
            parse_mode="HTML"
        )
        return

    new_url = parts[1].strip()
    if not (new_url.startswith("https://") or new_url.startswith("http://")):
        await message.answer("⚠️ Manzil https:// bilan boshlanishi kerak!")
        return

    WEBAPP_URL = new_url
    try:
        await bot.set_chat_menu_button(
            chat_id=message.chat.id,
            menu_button=MenuButtonWebApp(
                text="🎓 Platforma",
                web_app=WebAppInfo(url=WEBAPP_URL)
            )
        )
    except Exception as e:
        logger.warning(f"Menyu tugmasini yangilashda xato: {e}")

    await message.answer(
        f"✅ <b>WebApp URL muvaffaqiyatli yangilandi:</b>\n<code>{WEBAPP_URL}</code>\n\n"
        f"Endi bot va menyu tugmasi ushbu manzil orqali ochiladi!",
        reply_markup=get_main_keyboard(WEBAPP_URL),
        parse_mode="HTML"
    )


# 5. WebApp-dan yuborilgan ma'lumotlarni qabul qilish (sendData)
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

            stars = "⭐️" * min(5, max(1, round(percent / 20)))
            badge = "🥇 A'lochi" if percent >= 80 else ("🥈 Yaxshi" if percent >= 60 else "🥉 Qoniqarli")

            text = (
                f"🎉 <b>Tabriklaymiz, test yakunlandi!</b>\n\n"
                f"📚 <b>Kurs:</b> {course_title}\n"
                f"📊 <b>Natija:</b> {score} / {total} ball ({percent}%)\n"
                f"🎖 <b>Daraja:</b> {badge} {stars}\n\n"
            )

            if percent >= 70:
                text += "✅ <i>Siz sertifikat olish talabini muvaffaqiyatli bajardingiz!</i>"
            else:
                text += "💡 <i>Bilimingizni mustahkamlash uchun darslarni takroran ko'rib chiqishingizni tavsiya qilamiz.</i>"

            await message.answer(text, parse_mode="HTML")

        elif action == "enroll":
            course_id = data.get("course_id", "kurs")
            await message.answer(
                f"✅ <b>Tabriklaymiz!</b> Siz <code>{course_id}</code> kursiga muvaffaqiyatli yozildingiz.\n"
                f"O'rganishni istalgan vaqtda WebApp orqali davom ettirishingiz mumkin!",
                parse_mode="HTML"
            )
        else:
            await message.answer(f"Ma'lumot saqlandi: {data}")

    except Exception as e:
        logger.error(f"WebApp ma'lumotlarini qabul qilishda xatolik: {e}")
        await message.answer("✅ Natijangiz qabul qilindi!")


# 6. Callback so'rovlari
@dp.callback_query(F.data == "show_courses")
async def cb_courses(callback: types.CallbackQuery):
    await callback.message.answer(
        "Platformamizdagi barcha interaktiv kurslarni WebApp orqali ko'ring:",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(text="🎓 WebApp-ga Kirish", web_app=WebAppInfo(url=WEBAPP_URL))
            ]]
        )
    )
    await callback.answer()


@dp.callback_query(F.data == "show_achievements")
async def cb_achievements(callback: types.CallbackQuery):
    user_name = callback.from_user.first_name
    await callback.message.answer(
        f"🏆 <b>{user_name}ning Yutuqlari:</b>\n\n"
        f"🎖 Faol Talaba nishoni\n"
        f"⭐️ Ro'yxatdan o'tganlik uchun 10 ball\n"
        f"📜 Sertifikatlar holati: <i>Platformada testlarni topshiring</i>\n\n"
        f"Barcha yutuqlaringizni ko'rish uchun profilni oching:",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(text="👤 Profilni Ko'rish", web_app=WebAppInfo(url=WEBAPP_URL))
            ]]
        ),
        parse_mode="HTML"
    )
    await callback.answer()


@dp.callback_query(F.data == "show_info")
async def cb_info(callback: types.CallbackQuery):
    await callback.message.answer(
        "ℹ️ <b>EduPlatform Telegram WebApp</b>\n\n"
        "Ushbu bot orqali istalgan qurilmada (mobil, planshet, kompyuter) "
        " zamonaviy dasturlash va IT kasblari bo'yicha interaktiv darslar olishingiz mumkin.\n\n"
        f"🌐 Web versiya: {WEBAPP_URL}",
        parse_mode="HTML"
    )
    await callback.answer()


# 7. Asosiy ishga tushirish funksiyasi
async def main():
    logger.info("EduBot ishga tushmoqda...")
    try:
        bot_info = await bot.get_me()
        logger.info(f"Bot muvaffaqiyatli ulandi: @{bot_info.username} (ID: {bot_info.id})")
        print(f"\n==========================================")
        print(f"🤖 Bot faol: @{bot_info.username}")
        print(f"🌐 WebApp URL: {WEBAPP_URL}")
        print(f"==========================================\n")
    except Exception as e:
        logger.warning(f"Bot ma'lumotlarini olishda ogohlantirish: {e}")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
