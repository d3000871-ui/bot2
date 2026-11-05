"""
EduPlatform & Bot - Unified Web & Telegram Bot Server
Maxsus Render.com va Netlify uchun ishlab chiqilgan.

Xususiyatlari:
1. Render portini ($PORT) tinglaydi va saytni (index.html, css, js) host qiladi.
2. Aiogram 3 Telegram botini bir vaqtning o'zida fonda yurgizadi.
3. Saytdan (/api/submit-quiz) kelgan test natijalarini to'g'ridan-to'g'ri bot orqali foydalanuvchiga yuboradi.
"""

import os
import json
import logging
import asyncio
from pathlib import Path
from aiohttp import web
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
    MenuButtonWebApp
)

# 1. Konfiguratsiya
PORT = int(os.getenv("PORT", 10000))
BOT_TOKEN = os.getenv("BOT_TOKEN", "9201806873:AAELTm5p88mK9yNIfMUHB9cI7yQLFnnjY4s")
WEBAPP_URL = os.getenv("WEBAPP_URL", "")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("EduServer")

BASE_DIR = Path(__file__).resolve().parent

# 2. Telegram Botni sozlash
bot = None
dp = Dispatcher()

if BOT_TOKEN and BOT_TOKEN != "BOT_TOKENINGIZNI_BU_YERGA_YOZING":
    try:
        bot = Bot(token=BOT_TOKEN)
    except Exception as e:
        logger.error(f"Botni ishga tushirishda xato: {e}")


def get_keyboard(url: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🚀 O'quv Platformasini Ochish",
                    web_app=WebAppInfo(url=url)
                )
            ],
            [
                InlineKeyboardButton(text="📚 Kurslar", callback_data="show_courses"),
                InlineKeyboardButton(text="🏆 Yutuqlarim", callback_data="show_achievements")
            ],
            [
                InlineKeyboardButton(text="🌐 Saytga o'tish", url=url)
            ]
        ]
    )


@dp.message(CommandStart())
async def bot_start(message: types.Message):
    global WEBAPP_URL
    user_name = message.from_user.first_name
    current_url = WEBAPP_URL or "https://edubot-platform.netlify.app"

    try:
        await bot.set_chat_menu_button(
            chat_id=message.chat.id,
            menu_button=MenuButtonWebApp(
                text="🎓 Platforma",
                web_app=WebAppInfo(url=current_url)
            )
        )
    except Exception as e:
        logger.warning(f"Menyu tugmasida xato: {e}")

    text = (
        f"Assalomu alaykum, <b>{user_name}</b>! 👋\n\n"
        f"🎓 <b>EduPlatform</b> – IT kasblar va dasturlash bo'yicha interaktiv ta'lim platformasiga xush kelibsiz!\n\n"
        f"Platformada interaktiv darslar, video qo'llanmalar va bilimlarni mustahkamlovchi testlar mavjud.\n\n"
        f"Boshlash uchun quyidagi tugmani bosing:"
    )
    await message.answer(text, reply_markup=get_keyboard(current_url), parse_mode="HTML")


@dp.message(Command("courses"))
async def bot_courses(message: types.Message):
    current_url = WEBAPP_URL or "https://edubot-platform.netlify.app"
    text = (
        "📖 <b>Mavjud O'quv Kurslari:</b>\n\n"
        "1. 🐍 Python Backend & Django (28 dars)\n"
        "2. 🤖 Telegram Botlar (Aiogram 3)\n"
        "3. 🌐 Zamonaviy Frontend & React (22 dars)\n"
        "4. 🧠 AI & Prompt Engineering (16 dars)\n"
        "5. 🎨 UI/UX Dizayn & Figma (18 dars)\n"
        "6. 🇬🇧 IT Mutaxassislari uchun Ingliz Tili\n\n"
        "Barcha darslar platforma ichida mavjud:"
    )
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text="🎓 Platformani Ochish", web_app=WebAppInfo(url=current_url))
        ]]
    )
    await message.answer(text, reply_markup=kb, parse_mode="HTML")


@dp.message(Command("seturl"))
async def bot_seturl(message: types.Message):
    global WEBAPP_URL
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await message.answer(
            f"Hozirgi WebApp manzili:\n<code>{WEBAPP_URL}</code>\n\n"
            f"O'zgartirish uchun: <code>/seturl https://sizning-saytingiz.onrender.com</code>",
            parse_mode="HTML"
        )
        return

    WEBAPP_URL = parts[1].strip()
    try:
        await bot.set_chat_menu_button(
            chat_id=message.chat.id,
            menu_button=MenuButtonWebApp(text="🎓 Platforma", web_app=WebAppInfo(url=WEBAPP_URL))
        )
    except Exception as e:
        logger.warning(f"Menyu tugmasida xato: {e}")

    await message.answer(
        f"✅ <b>WebApp URL yangilandi:</b>\n<code>{WEBAPP_URL}</code>",
        reply_markup=get_keyboard(WEBAPP_URL),
        parse_mode="HTML"
    )


@dp.message(F.web_app_data)
async def bot_webapp_data(message: types.Message):
    try:
        data = json.loads(message.web_app_data.data)
        action = data.get("action")

        if action == "quiz_completed":
            course_title = data.get("course_title", "Kurs")
            score = data.get("score", 0)
            total = data.get("total", 0)
            percent = round((score / total) * 100) if total > 0 else 0

            stars = "⭐️" * min(5, max(1, round(percent / 20)))
            text = (
                f"🎉 <b>Tabriklaymiz, test yakunlandi!</b>\n\n"
                f"📚 <b>Kurs:</b> {course_title}\n"
                f"📊 <b>Natija:</b> {score} / {total} ball ({percent}%)\n"
                f"Baho: {stars}\n\n"
            )
            if percent >= 70:
                text += "✅ <i>A'lo natija! Siz kurs talablarini bajardingiz.</i>"
            else:
                text += "💡 <i>Darslarni yana bir bor takrorlab, bilimingizni oshirishingiz mumkin.</i>"

            await message.answer(text, parse_mode="HTML")
        elif action == "enroll":
            course_id = data.get("course_id", "kurs")
            await message.answer(f"✅ <b>{course_id}</b> kursiga muvaffaqiyatli a'zo bo'ldingiz!", parse_mode="HTML")
    except Exception as e:
        logger.error(f"Xato: {e}")
        await message.answer("Natija saqlandi!")


@dp.callback_query(F.data == "show_courses")
async def cb_courses(callback: types.CallbackQuery):
    url = WEBAPP_URL or "https://edubot-platform.netlify.app"
    await callback.message.answer(
        "Darslarni boshlash uchun platformaga kiring:",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(text="🎓 WebApp-ni Ochish", web_app=WebAppInfo(url=url))
            ]]
        )
    )
    await callback.answer()


@dp.callback_query(F.data == "show_achievements")
async def cb_achievements(callback: types.CallbackQuery):
    url = WEBAPP_URL or "https://edubot-platform.netlify.app"
    await callback.message.answer(
        "🏆 Profilingiz va olingan ballaringiz platformaning 'Profil' qismida saqlanadi:",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(text="👤 Profilni Ochish", web_app=WebAppInfo(url=url))
            ]]
        )
    )
    await callback.answer()


# 3. HTTP Web Server Handlers (Render uchun)
async def handle_index(request):
    """Asosiy sahifani (index.html) uzatish"""
    index_file = BASE_DIR / "index.html"
    return web.FileResponse(index_file)


async def handle_health(request):
    """Render salomatlik tekshiruvi (Health check)"""
    bot_status = "connected" if bot else "not_configured"
    return web.json_response({
        "status": "healthy",
        "service": "EduPlatform Web & Bot Server",
        "bot_status": bot_status,
        "webapp_url": WEBAPP_URL
    })


async def handle_api_config(request):
    """Frontend uchun bot sozlamalari"""
    username = "Noma'lum"
    if bot:
        try:
            me = await bot.get_me()
            username = me.username
        except Exception:
            pass
    return web.json_response({
        "bot_username": username,
        "bot_token_configured": bool(bot),
        "webapp_url": WEBAPP_URL
    })


async def handle_submit_quiz(request):
    """Saytdan test natijalarini qabul qilish va botga yuborish"""
    try:
        body = await request.json()
        user_id = body.get("user_id")
        course_title = body.get("course_title", "Kurs")
        score = body.get("score", 0)
        total = body.get("total", 0)

        percent = round((score / total) * 100) if total > 0 else 0

        # Agar Telegram user_id mavjud bo'lsa, to'g'ridan-to'g'ri foydalanuvchiga Telegram orqali xabar yuboramiz
        if bot and user_id:
            try:
                await bot.send_message(
                    chat_id=user_id,
                    text=(
                        f"📊 <b>EduPlatform Test Natijasi:</b>\n\n"
                        f"📚 Kurs: <b>{course_title}</b>\n"
                        f"🎯 Natija: <b>{score}/{total}</b> ({percent}%)\n\n"
                        f"{'🎉 Ajoyib, bilimingiz tasdiqlandi!' if percent >= 70 else '💡 Yana bir bor urinib ko\'ring!'}"
                    ),
                    parse_mode="HTML"
                )
            except Exception as e:
                logger.warning(f"Telegramga xabar jo'natilmadi: {e}")

        return web.json_response({"success": True, "message": "Natija qabul qilindi!"})
    except Exception as e:
        logger.error(f"Test submit xatosi: {e}")
        return web.json_response({"success": False, "error": str(e)}, status=400)


# 4. Background Bot Runner (aiohttp bilan integratsiya)
async def start_background_bot(app):
    if bot:
        logger.info("Telegram Bot polling boshlanmoqda...")
        app['bot_task'] = asyncio.create_task(dp.start_polling(bot))


async def cleanup_background_bot(app):
    if 'bot_task' in app:
        app['bot_task'].cancel()
        try:
            await app['bot_task']
        except asyncio.CancelledError:
            pass
    if bot:
        await bot.session.close()


def create_app():
    app = web.Application()

    # Statik fayllar (css va js)
    css_dir = BASE_DIR / "css"
    js_dir = BASE_DIR / "js"
    if css_dir.exists():
        app.router.add_static("/css/", path=str(css_dir), name="css")
    if js_dir.exists():
        app.router.add_static("/js/", path=str(js_dir), name="js")

    # Marshrutlar
    app.router.add_get("/", handle_index)
    app.router.add_get("/index.html", handle_index)
    app.router.add_get("/health", handle_health)
    app.router.add_get("/api/config", handle_api_config)
    app.router.add_post("/api/submit-quiz", handle_submit_quiz)

    # Botni aiohttp hayot sikli bilan boshqarish
    app.on_startup.append(start_background_bot)
    app.on_cleanup.append(cleanup_background_bot)

    return app


if __name__ == "__main__":
    logger.info(f"EduServer port {PORT} da ishga tushmoqda...")
    app = create_app()
    web.run_app(app, host="0.0.0.0", port=PORT)
