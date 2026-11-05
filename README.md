# 🎓 EduPlatform - Telegram WebApp O'quv Platformasi

Zamonaviy, qulay va interaktiv IT ta'lim platformasi. Ushbu loyiha ham veb-brauzerda, ham **Telegram WebApp (Mini App)** sifatida to'liq ishlaydi va Telegram bot bilan integratsiya qilingan.

[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/d3000871-ui/bot2)
[![Deploy to Render (Free)](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/d3000871-ui/bot2)

---

## 🤖 Bot Ma'lumotlari

- **Bot Tokeni:** `9201806873:AAELTm5p88mK9yNIfMUHB9cI7yQLFnnjY4s`
- **Integratsiya turlari:**
  1. **Telegram WebApp SDK:** Foydalanuvchi ismi, avatari va Telegram ranglari avtomatik yuklanadi.
  2. **Boshqaruv menyusi (Menu Button):** Botning pastki chap qismidagi "🎓 Platforma" tugmasi orqali istalgan vaqtda platformani to'liq ekranda ochish mumkin.
  3. **Interaktiv test natijalari:** Saytdagi testlar topshirilgach, natijalar ball, foiz va yutuq nishonlari bilan birga to'g'ridan-to'g'ri Telegram botga xabar shaklida yuboriladi.
  4. **Sayt orqali botga o'tish:** Agar foydalanuvchi oddiy kompyuter brauzerida ochsa, yuqori qismdagi banner va suzuvchi Telegram tugmasi orqali botga 1 bosishda o'tishi mumkin.

---

## 🚀 Render.com ga 100% BEPUL Deploy Qilish (Karta talab qilinmaydi)

Render.com da bot va saytni **Free Tier ($0/oylik)** rejimida bank kartasi kiritmasdan ishga tushirish:

### 1-usul: Render Blueprint orqali (Avtomatik Free Plan)
1. Render-da chiqqan to'lov oynasini **"Cancel"** qiling yoki sahifani yangilang (F5).
2. [dashboard.render.com/blueprints](https://dashboard.render.com/blueprints) sahifasiga o'ting.
3. `bot2` ([https://github.com/d3000871-ui/bot2](https://github.com/d3000871-ui/bot2)) reponi tanlang.
4. `render.yaml` faylida `plan: free` sozlanganligi sababli Render endi karta ma'lumotlarini so'ramaydi!
5. **"Apply"** tugmasini bosing.

### 2-usul: Qo'lda Web Service ochish (Eng ishonchli usul)
1. [dashboard.render.com](https://dashboard.render.com/) ga kiring -> **"+ New"** -> **"Web Service"** ni bosing.
2. `bot2` reponi tanlang.
3. Quyidagi sozlamalarni kiriting:
   - **Name:** `edubot-platform`
   - **Language / Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python server.py`
   - **Instance Type:** **Free ($0/month)** ni tanlang.
4. **Environment Variables** bo'limida:
   - `BOT_TOKEN` = `9201806873:AAELTm5p88mK9yNIfMUHB9cI7yQLFnnjY4s`
5. **"Create Web Service"** tugmasini bosing!

---

## ⚡ Netlify-ga Deploy Qilish (Muqobil)

Saytni Netlify orqali tezyurar CDN-da bepul ochish:
1. [app.netlify.com](https://app.netlify.com) saytiga kiring -> **"Add new site"** -> **"Import an existing project"**.
2. **GitHub** orqali `bot2` reponi tanlang.
3. **Publish directory:** `.` (nuqta).
4. **"Deploy site"** tugmasini bosing.
5. Chiqqan havola (masalan, `https://bot2-edu.netlify.app`)ni botga o'rnatish uchun Telegramda botingizga yozing:
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

---

Muallif: [d3000871-ui](https://github.com/d3000871-ui)  
Repo: [https://github.com/d3000871-ui/bot2.git](https://github.com/d3000871-ui/bot2.git)
