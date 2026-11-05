# 🎓 EduPlatform - Telegram WebApp O'quv Platformasi

Zamonaviy, qulay va interaktiv ta'lim platformasi. Ushbu loyiha ham oddiy veb-brauzerda, ham **Telegram WebApp (Mini App)** sifatida to'liq ishlaydi va Telegram bot bilan integratsiya qilingan.

[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/d3000871-ui/bot2)

---

## ✨ Loyiha Imkoniyatlari

- 📱 **Telegram Mini App Integratsiyasi**:
  - `Telegram.WebApp` SDK orqali foydalanuvchi ma'lumotlarini avtomatik aniqlash (Ism, avatar).
  - Telegram ranglar mavzusiga moslashish (Dark / Light mode).
  - Haptic feedback (tugmalarni bosganda tebranish effekti).
  - Natijalarni to'g'ridan-to'g'ri Telegram botga yuborish (`sendData`).
- 📚 **Kurslar Katalogi**:
  - Python va Backend (Django)
  - Telegram Bot yaratish (Aiogram 3)
  - Zamonaviy Frontend & React
  - Sun'iy Intellekt (AI) & Prompt muhandisligi
  - UI/UX Dizayn (Figma)
  - IT uchun Ingliz tili
- 🎥 **Interaktiv Darslar Rejasi (Syllabus)**: Har bir kurs darslari, videopleer simulyatsiyasi va darslarni o'zlashtirish belgisi.
- 📝 **Viktorina va Test (Quiz) Tizimi**:
  - Har bir kurs bo'yicha amaliy savollar va ballar hisobi.
  - Test yakunida natijani Telegram botga yuborish.
- 👤 **Shaxsiy Profil va Yutuqlar**:
  - O'rganilgan darslar soni, faollik nishonlari va sertifikatlar statistikasi.
- 🔍 **Qidiruv va Kategoriya Filtrlari**: Tezkor qidirish imkoniyati.

---

## 🚀 Netlify-ga Deploy Qilish

Sayt to'liq statik (HTML5, CSS3, JavaScript) bo'lgani uchun **Netlify** platformasida 1 daqiqada bepul ishga tushadi:

### 1-usul: GitHub orqali (Tavsiya etiladi - Continuous Deployment)
1. [Netlify.com](https://app.netlify.com) saytiga kiring va ro'yxatdan o'ting / kiring.
2. **"Add new site"** -> **"Import an existing project"** ni bosing.
3. **GitHub** provayderini tanlang va `bot2` (https://github.com/d3000871-ui/bot2) reponi tanlang.
4. Build sozlamalari:
   - **Branch to deploy:** `main` (yoki `master`)
   - **Publish directory:** `.`
5. **"Deploy site"** tugmasini bosing!
6. Netlify sizga havola taqdim etadi (masalan: `https://sizning-saytingiz.netlify.app`).

### 2-usul: Bir martalik tugma orqali
Yuqoridagi **"Deploy to Netlify"** tugmasini bosing va o'z hisobingizga yuklang.

---

## 🤖 Telegram Botni Sozlash va Ishga Tushirish

### 1. Bot yaratish (@BotFather)
1. Telegramda [@BotFather](https://t.me/BotFather) botiga kiring.
2. `/newbot` buyrug'ini yuboring va botingiz nomini kiriting.
3. Olingan **HTTP API Token**ni saqlab oling.

### 2. WebApp Menyu tugmasini yoqish
1. [@BotFather](https://t.me/BotFather) ga kiring.
2. `/mybots` -> Botingizni tanlang -> **"Bot Settings"** -> **"Menu Button"** -> **"Configure menu button"**.
3. Netlify-dagi havolangizni yuboring (masalan: `https://sizning-saytingiz.netlify.app`).
4. Tugma nomini kiriting (masalan: `🎓 Platforma`).

### 3. Python Botni ishga tushirish:
```bash
# Kerakli kutubxonani o'rnatish
pip install -r requirements.txt

# bot.py faylidagi BOT_TOKEN va WEBAPP_URL ni o'zgartiring, yoki muhit o'zgaruvchilari orqali:
export BOT_TOKEN="SIZNING_BOT_TOKENINGIZ"
export WEBAPP_URL="https://sizning-saytingiz.netlify.app"

# Ishga tushirish
python bot.py
```

---

## 📁 Fayllar Tuzilishi

```text
├── index.html            # Asosiy HTML interfeys (Telegram WebApp & Landing)
├── css/
│   └── style.css         # Zamonaviy dizayn, dark/light mavzu, mobil moslashuv
├── js/
│   └── app.js           # Kurslar bazasi, testlar, Telegram WebApp API
├── bot.py                # Aiogram 3 da yozilgan Telegram bot
├── netlify.toml          # Netlify server sozlamalari va Telegram iframe ruxsatlari
├── _headers              # X-Frame-Options va xavfsizlik sozlamalari
├── _redirects            # SPA yo'naltirish qoidalari
├── requirements.txt      # Python paketlari
├── .gitignore            # Git istisno fayllari
└── README.md             # Qo'llanma
```

---

Muallif: [d3000871-ui](https://github.com/d3000871-ui)
