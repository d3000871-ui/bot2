# 🎓 EduPlatform - Telegram WebApp O'quv Platformasi

Zamonaviy, qulay va interaktiv IT ta'lim platformasi. Ushbu loyiha ham veb-brauzerda, ham **Telegram WebApp (Mini App)** sifatida to'liq ishlaydi va Telegram bot bilan integratsiya qilingan.

[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/d3000871-ui/bot2)
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/d3000871-ui/bot2)

---

## 🤖 Bot Ma'lumotlari

- **Bot Tokeni:** `9201806873:AAELTm5p88mK9yNIfMUHB9cI7yQLFnnjY4s`
- **Integratsiya turlari:**
  1. **Telegram WebApp SDK:** Foydalanuvchi ismi, avatari va Telegram ranglari avtomatik yuklanadi.
  2. **Boshqaruv menyusi (Menu Button):** Botning pastki chap qismidagi "🎓 Platforma" tugmasi orqali istalgan vaqtda platformani to'liq ekranda ochish mumkin.
  3. **Interaktiv test natijalari:** Saytdagi testlar topshirilgach, natijalar ball, foiz va yutuq nishonlari bilan birga to'g'ridan-to'g'ri Telegram botga xabar shaklida yuboriladi.
  4. **Sayt orqali botga o'tish:** Agar foydalanuvchi oddiy kompyuter brauzerida ochsa, yuqori qismdagi banner va suzuvchi Telegram tugmasi orqali botga 1 bosishda o'tishi mumkin.

---

## 🚀 Render.com ga Deploy Qilish (Qadam-ba-qadam)

Render.com da bot va saytni **bitta bepul Web Service** sifatida bir vaqtning o'zida yurgizish mumkin:

### 1-usul: Render Blueprint (Avtomatik - Eng osoni)
1. [dashboard.render.com](https://dashboard.render.com/) sahifasiga kiring.
2. **"New +"** tugmasini bosing va **"Blueprint"** ni tanlang.
3. GitHub hisobingizdagi `bot2` ([https://github.com/d3000871-ui/bot2](https://github.com/d3000871-ui/bot2)) reponi tanlang.
4. Render loyihangizdagi `render.yaml` faylini avtomatik o'qiydi va sozlaydi.
5. **"Apply"** tugmasini bosing! Bir necha daqiqada saytingiz va botingiz ishga tushadi.

### 2-usul: Qo'lda Web Service yaratish
1. [dashboard.render.com](https://dashboard.render.com/) da **"New +"** -> **"Web Service"** ni bosing.
2. `bot2` reponi tanlang.
3. Sozlamalar:
   - **Name:** `edubot-platform`
   - **Language:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python server.py`
4. **Environment Variables** (Muhit o'zgaruvchilari) bo'limida:
   - `BOT_TOKEN` = `9201806873:AAELTm5p88mK9yNIfMUHB9cI7yQLFnnjY4s`
   - `WEBAPP_URL` = `https://sizning-servisingiz.onrender.com` (yoki Netlify manzilingiz)
5. **"Create Web Service"** tugmasini bosing.

---

## ⚡ Netlify-ga Deploy Qilish

Agar saytingizni Netlify-da alohida tezyurar CDN orqali joylamoqchi bo'lsangiz:
1. [app.netlify.com](https://app.netlify.com) saytiga kiring.
2. **"Add new site"** -> **"Import an existing project"** -> **GitHub** -> `bot2` reponi tanlang.
3. **Publish directory:** `.` (nuqta).
4. **"Deploy site"** tugmasini bosing.
5. Chiqqan havola (masalan, `https://bot2-edu.netlify.app`)ni botga o'rnatish uchun Telegramda botingizga quyidagicha yozing:
   `/seturl https://bot2-edu.netlify.app`

---

## 💻 Mahalliy Kompyuterda Ishga Tushirish

```bash
# Kerakli kutubxonalarni o'rnatish
pip install -r requirements.txt

# Web Sayt + Botni birga ishga tushirish (Render rejimi)
python server.py

# Yoki faqat botning o'zini ishga tushirish
python bot.py
```

Brauzerda [http://localhost:10000](http://localhost:10000) manzilini ochib platformani tekshirishingiz mumkin.

---

## 📁 Fayllar Strukturasi

```text
├── index.html            # Asosiy veb-ilova va Telegram WebApp sahifasi
├── css/
│   └── style.css         # Zamonaviy mobil va dark-mode dizayn
├── js/
│   └── app.js           # Kurslar bazasi, testlar, Telegram WebApp integratsiyasi
├── server.py             # Render uchun Web-server + Telegram bot birlashgan server
├── bot.py                # Alohida Telegram bot skripti (Aiogram 3)
├── render.yaml           # Render.com Blueprint sozlamalari
├── Procfile              # Render / PaaS ishga tushirish buyrug'i
├── runtime.txt           # Python versiyasi
├── netlify.toml          # Netlify sozlamalari va Telegram iframe ruxsatlari
├── requirements.txt      # Aiogram va Aiohttp paketlari
└── README.md             # To'liq qo'llanma
```

---

Muallif: [d3000871-ui](https://github.com/d3000871-ui)
Repo: [https://github.com/d3000871-ui/bot2.git](https://github.com/d3000871-ui/bot2.git)
