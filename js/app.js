/**
 * EduPlatform - Telegram WebApp & O'quv Platformasi
 * Muallif: d3000871-ui
 */

// 1. Kurslar Ma'lumotlar Bazasi
const COURSES = [
  {
    id: 'tg-bot',
    title: 'Telegram Botlar Yaratish (Python & Aiogram)',
    category: 'programming',
    badge: 'hot',
    badgeText: 'Mashhur 🔥',
    icon: 'fa-brands fa-telegram',
    iconBg: '#0088cc',
    iconColor: '#ffffff',
    mentor: 'Azizbek Rahimov',
    rating: 4.9,
    students: 1420,
    lessonsCount: 14,
    duration: '18 soat',
    description: 'Noldan boshlab murakkab Telegram botlar, WebApp (Mini App), to\'lov tizimlari va avtomatlashtirish botlarini ishlab chiqish.',
    syllabus: [
      { id: 1, title: 'Kirish: Telegram Bot API qanday ishlaydi?', duration: '12 daq', video: 'https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ' },
      { id: 2, title: 'Aiogram 3 o\'rnatish va birinchi /start buyrug\'i', duration: '20 daq' },
      { id: 3, title: 'Inline klaviaturalar va Callback so\'rovlari', duration: '25 daq' },
      { id: 4, title: 'FSM (Finite State Machine) bilan ro\'yxatdan o\'tish', duration: '32 daq' },
      { id: 5, title: 'Telegram WebApp integratsiyasi (HTML & JS)', duration: '40 daq' },
      { id: 6, title: 'PostgreSQL bazasi bilan bog\'lash', duration: '35 daq' },
      { id: 7, title: 'Botni serverga (VPS/Railway) joylash', duration: '28 daq' }
    ],
    quiz: [
      {
        question: 'Telegram bot yaratish uchun qaysi rasmiy botdan API Token olinadi?',
        options: ['@BotFather', '@TelegramManager', '@ApiBot', '@TokenMaster'],
        answer: 0
      },
      {
        question: 'Telegram WebApp sahifasini to\'liq ekranga yoyish uchun qaysi metod chaqiriladi?',
        options: ['Telegram.WebApp.full()', 'Telegram.WebApp.expand()', 'Telegram.WebApp.openFull()', 'Telegram.WebApp.maximize()'],
        answer: 1
      },
      {
        question: 'Aiogram 3 da yangi buyruqni tutish qanday belgilanadi?',
        options: ['@dp.command("start")', '@dp.message(Command("start"))', '@bot.on_command("start")', '@router.catch("start")'],
        answer: 1
      }
    ]
  },
  {
    id: 'frontend',
    title: 'Zamonaviy Frontend & React Kursi',
    category: 'web',
    badge: 'new',
    badgeText: 'Yangi ✨',
    icon: 'fa-brands fa-react',
    iconBg: '#20232a',
    iconColor: '#61dafb',
    mentor: 'Farrux Umarov',
    rating: 4.8,
    students: 2150,
    lessonsCount: 22,
    duration: '32 soat',
    description: 'HTML5, CSS3, JavaScript ES6+ hamda React.js orqali interaktiv, chiroyli va tezkor veb-saytlar yaratish.',
    syllabus: [
      { id: 1, title: 'HTML5 semantik teglari va zamonaviy strukturasi', duration: '18 daq' },
      { id: 2, title: 'Flexbox va CSS Grid bilan moslashuvchan dizayn', duration: '30 daq' },
      { id: 3, title: 'JavaScript Asoslari: Dom manipulyatsiyasi', duration: '45 daq' },
      { id: 4, title: 'React komponentlari, State va Props tushunchasi', duration: '50 daq' },
      { id: 5, title: 'API bilan ishlash (Fetch & Axios)', duration: '35 daq' }
    ],
    quiz: [
      {
        question: 'HTML5 da sahifaning asosiy navigatsiya menyusi uchun qaysi teg ishlatiladi?',
        options: ['<menu>', '<nav>', '<header>', '<navigation>'],
        answer: 1
      },
      {
        question: 'CSS da elementlarni ekranning markaziga tekislashning eng oson usuli qaysi?',
        options: ['display: flex; justify-content: center; align-items: center;', 'float: center;', 'align: middle;', 'margin: auto center;'],
        answer: 0
      }
    ]
  },
  {
    id: 'python-dev',
    title: 'Python Dasturlash & Backend (Django)',
    category: 'programming',
    badge: 'cat',
    badgeText: 'Top Kurs',
    icon: 'fa-brands fa-python',
    iconBg: '#3776ab',
    iconColor: '#ffd343',
    mentor: 'Rustam Qosimov',
    rating: 4.95,
    students: 3100,
    lessonsCount: 28,
    duration: '40 soat',
    description: 'Noldan professional backend dasturchi bo\'lish yo\'li. Algoritmlar, OOP, ma\'lumotlar tuzilmasi va Django REST Framework.',
    syllabus: [
      { id: 1, title: 'Python asoslari: Sintaksis va o\'zgaruvchilar', duration: '20 daq' },
      { id: 2, title: 'Ma\'lumotlar turlari: List, Dict, Tuple, Set', duration: '35 daq' },
      { id: 3, title: 'OOP (Obyektga yo\'naltirilgan dasturlash)', duration: '45 daq' },
      { id: 4, title: 'Django loyihasi tuzilishi va Migrationlar', duration: '40 daq' }
    ],
    quiz: [
      {
        question: 'Pythonda o\'zgarmas (immutable) ma\'lumot turi qaysi?',
        options: ['list', 'dict', 'tuple', 'set'],
        answer: 2
      },
      {
        question: 'Pythonda funksiya qaysi kalit so\'z orqali e\'lon qilinadi?',
        options: ['function', 'def', 'func', 'fn'],
        answer: 1
      }
    ]
  },
  {
    id: 'ai-prompt',
    title: 'Sun\'iy Intellekt & Prompt Engineering',
    category: 'ai',
    badge: 'new',
    badgeText: 'Trend 🔥',
    icon: 'fa-solid fa-brain',
    iconBg: '#7c3aed',
    iconColor: '#ffffff',
    mentor: 'Shahzod Aliyev',
    rating: 4.92,
    students: 980,
    lessonsCount: 16,
    duration: '15 soat',
    description: 'ChatGPT, Gemini, Claude va Midjourney imkoniyatlaridan biznes va dasturlashda 10 barobar unumli foydalanish sirlari.',
    syllabus: [
      { id: 1, title: 'LLM modellari qanday fikrlaydi?', duration: '15 daq' },
      { id: 2, title: 'Samarali Prompt yozish formulalari', duration: '25 daq' },
      { id: 3, title: 'AI agentlar va avtomatlashtirish tizimlari', duration: '35 daq' }
    ],
    quiz: [
      {
        question: 'LLM qisqartmasining to\'liq ma\'nosi nima?',
        options: ['Large Language Model', 'Low Level Machine', 'Live Learning Method', 'Logical Linear Matrix'],
        answer: 0
      }
    ]
  },
  {
    id: 'ui-ux',
    title: 'UI/UX Dizayn & Figma Prototip',
    category: 'design',
    badge: 'cat',
    badgeText: 'Amaliy',
    icon: 'fa-brands fa-figma',
    iconBg: '#f24e1e',
    iconColor: '#ffffff',
    mentor: 'Dildora Karimova',
    rating: 4.85,
    students: 1100,
    lessonsCount: 18,
    duration: '22 soat',
    description: 'Foydalanuvchi interfeysi (UI) va tajribasi (UX) yaratish qoidalari, Figmada komponentlar va dizayn tizimlari.',
    syllabus: [
      { id: 1, title: 'UI/UX nima va ular orasidagi farq', duration: '15 daq' },
      { id: 2, title: 'Figma asboblari va Auto-layout', duration: '30 daq' }
    ],
    quiz: [
      {
        question: 'Figmada elementlarni avtomatik joylashtirish qaysi xususiyat orqali qilinadi?',
        options: ['Auto Layout', 'Flexbox', 'Smart Position', 'Group Arrange'],
        answer: 0
      }
    ]
  },
  {
    id: 'english-it',
    title: 'IT Mutaxassislari Uchun Ingliz Tili',
    category: 'languages',
    badge: 'cat',
    badgeText: 'Muhim ⭐',
    icon: 'fa-solid fa-language',
    iconBg: '#059669',
    iconColor: '#ffffff',
    mentor: 'Malika Saidova',
    rating: 4.9,
    students: 2400,
    lessonsCount: 20,
    duration: '25 soat',
    description: 'Xorijiy kompaniyalar suhbatidan o\'tish, texnik hujjatlarni erkin o\'qish va muloqot qilish ko\'nikmalari.',
    syllabus: [
      { id: 1, title: 'Texnik lug\'at va atamalar bazasi', duration: '20 daq' },
      { id: 2, title: 'Job Interview: O\'zini tanishtirish san\'ati', duration: '30 daq' }
    ],
    quiz: [
      {
        question: 'IT suhbatida "Tell me about yourself" savoliga qanday javob berish to\'g\'ri?',
        options: ['Kasbiy tajriba va loyihalarga urg\'u berish', 'Bolalik haqida so\'zlash', 'Faqat maosh haqida gapirish', 'Hamma kurslarni birma-bir sanash'],
        answer: 0
      }
    ]
  }
];

// 2. Ilova Holati (State)
let appState = {
  currentCategory: 'all',
  searchQuery: '',
  activeCourse: null,
  activeLessonIndex: 0,
  enrolledCourses: JSON.parse(localStorage.getItem('edu_enrolled') || '["tg-bot"]'),
  completedLessons: JSON.parse(localStorage.getItem('edu_completed') || '{}'),
  quizScores: JSON.parse(localStorage.getItem('edu_scores') || '{}'),
  theme: localStorage.getItem('edu_theme') || 'light',
  user: {
    id: null,
    firstName: "O'quvchi",
    lastName: '',
    username: ''
  }
};

// 3. Telegram WebApp integratsiyasi
const tg = window.Telegram?.WebApp;

function initTelegram() {
  if (tg) {
    tg.ready();
    tg.expand();
    document.body.classList.add('telegram-app');

    // Foydalanuvchi ma'lumotlarini olish
    if (tg.initDataUnsafe && tg.initDataUnsafe.user) {
      const u = tg.initDataUnsafe.user;
      appState.user.id = u.id;
      appState.user.firstName = u.first_name || "O'quvchi";
      appState.user.lastName = u.last_name || '';
      appState.user.username = u.username ? `@${u.username}` : '';
      
      const avatarEl = document.getElementById('userAvatar');
      const nameEl = document.getElementById('userNameHeader');
      if (avatarEl) avatarEl.textContent = appState.user.firstName.charAt(0).toUpperCase();
      if (nameEl) nameEl.textContent = appState.user.firstName;
    }

    // Telegram mavzusiga moslashish
    if (tg.colorScheme === 'dark') {
      setTheme('dark');
    }
  }
}

// Haptic tebranish funksiyasi
function triggerHaptic(type = 'light') {
  if (tg?.HapticFeedback) {
    tg.HapticFeedback.impactOccurred(type);
  }
}

// 4. UI Render funksiyalari
function renderCourses() {
  const container = document.getElementById('courseGrid');
  if (!container) return;

  const filtered = COURSES.filter(course => {
    const matchCat = appState.currentCategory === 'all' || course.category === appState.currentCategory;
    const matchSearch = course.title.toLowerCase().includes(appState.searchQuery.toLowerCase()) ||
                        course.description.toLowerCase().includes(appState.searchQuery.toLowerCase()) ||
                        course.mentor.toLowerCase().includes(appState.searchQuery.toLowerCase());
    return matchCat && matchSearch;
  });

  const countEl = document.getElementById('coursesCount');
  if (countEl) countEl.textContent = `${filtered.length} ta kurs`;

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="text-align: center; padding: 40px 20px; color: var(--text-muted);">
        <i class="fa-solid fa-magnifying-glass" style="font-size: 2.5rem; margin-bottom: 12px; opacity: 0.5;"></i>
        <p style="font-size: 1rem; font-weight: 600;">Hech qanday kurs topilmadi</p>
        <p style="font-size: 0.85rem;">Qidiruv so'zini o'zgartirib ko'ring yoki boshqa toifani tanlang.</p>
      </div>
    `;
    return;
  }

  container.innerHTML = filtered.map(course => {
    const isEnrolled = appState.enrolledCourses.includes(course.id);
    const completedCount = (appState.completedLessons[course.id] || []).length;
    const progressPercent = Math.round((completedCount / course.syllabus.length) * 100);

    return `
      <div class="course-card" onclick="openCourseModal('${course.id}')">
        <div class="course-top">
          <div class="course-icon-box" style="background: ${course.iconBg}; color: ${course.iconColor};">
            <i class="${course.icon}"></i>
          </div>
          <div class="course-info">
            <div class="badge-row">
              <span class="badge ${course.badge === 'hot' ? 'badge-hot' : course.badge === 'new' ? 'badge-new' : 'badge-cat'}">
                ${course.badgeText}
              </span>
            </div>
            <h3 class="course-title">${course.title}</h3>
            <div class="course-mentor">
              <i class="fa-solid fa-chalkboard-user"></i> ${course.mentor}
            </div>
          </div>
        </div>

        ${isEnrolled ? `
          <div class="course-progress-wrap">
            <div class="progress-header">
              <span>Jarayon: ${completedCount}/${course.syllabus.length} dars</span>
              <span>${progressPercent}%</span>
            </div>
            <div class="progress-bar-bg">
              <div class="progress-bar-fill" style="width: ${progressPercent}%"></div>
            </div>
          </div>
        ` : ''}

        <div class="course-meta">
          <div class="meta-group">
            <span class="meta-item"><i class="fa-solid fa-star" style="color: #f59e0b;"></i> ${course.rating}</span>
            <span class="meta-item"><i class="fa-solid fa-users"></i> ${course.students}</span>
            <span class="meta-item"><i class="fa-solid fa-clock"></i> ${course.duration}</span>
          </div>
          <button class="course-btn">
            ${isEnrolled ? 'Davom etish' : 'Boshlash'}
          </button>
        </div>
      </div>
    `;
  }).join('');
}

// 5. Kurs Tafsilotlari Modalini Ochish
window.openCourseModal = function(courseId) {
  triggerHaptic('light');
  const course = COURSES.find(c => c.id === courseId);
  if (!course) return;

  appState.activeCourse = course;
  appState.activeLessonIndex = 0;

  const modal = document.getElementById('courseModal');
  const modalTitle = document.getElementById('modalCourseTitle');
  const modalBody = document.getElementById('modalCourseBody');

  modalTitle.textContent = course.title;
  
  const isEnrolled = appState.enrolledCourses.includes(course.id);
  const completedList = appState.completedLessons[course.id] || [];

  modalBody.innerHTML = `
    <!-- Video Player Simulator -->
    <div class="player-container">
      <div class="video-screen">
        <div class="play-pulse-btn" onclick="playLessonVideo()">
          <i class="fa-solid fa-play"></i>
        </div>
        <h4 id="videoLessonTitle" style="font-size: 1.05rem; font-weight: 700;">${course.syllabus[0].title}</h4>
        <p style="font-size: 0.8rem; opacity: 0.8; margin-top: 4px;">Davomiyligi: ${course.syllabus[0].duration}</p>
      </div>
    </div>

    <!-- Kurs Ta'rifi -->
    <div style="margin-bottom: 20px;">
      <h4 style="font-size: 1rem; font-weight: 700; margin-bottom: 6px;">Kurs haqida</h4>
      <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.6;">${course.description}</p>
    </div>

    <!-- Darslar ro'yxati (Syllabus) -->
    <div class="syllabus-title">
      <span>Darslar Rejasi</span>
      <span style="font-size: 0.82rem; color: var(--text-muted); font-weight: 500;">${course.syllabus.length} ta dars</span>
    </div>

    <div class="lesson-list">
      ${course.syllabus.map((lesson, idx) => {
        const isDone = completedList.includes(lesson.id);
        const isActive = idx === appState.activeLessonIndex;
        return `
          <div class="lesson-item ${isActive ? 'active' : ''} ${isDone ? 'completed' : ''}" onclick="selectLesson(${idx})">
            <div class="lesson-item-left">
              <div class="lesson-status-icon">
                ${isDone ? '<i class="fa-solid fa-check"></i>' : (idx + 1)}
              </div>
              <div>
                <div class="lesson-title-text">${lesson.title}</div>
                <div class="lesson-duration"><i class="fa-regular fa-clock"></i> ${lesson.duration}</div>
              </div>
            </div>
            <i class="fa-solid fa-play" style="font-size: 0.8rem; color: var(--text-muted);"></i>
          </div>
        `;
      }).join('')}
    </div>

    <!-- Amallar: Test va Kursga a'zo bo'lish -->
    <div class="course-actions">
      ${!isEnrolled ? `
        <button class="btn-primary" onclick="enrollCourse('${course.id}')">
          <i class="fa-solid fa-user-plus"></i> Kursga Yozilish (Bepul)
        </button>
      ` : `
        <button class="btn-primary" onclick="openQuizModal('${course.id}')">
          <i class="fa-solid fa-clipboard-question"></i> Bilimni Sinash (Test)
        </button>
        <button class="btn-secondary" onclick="markLessonComplete('${course.id}')">
          <i class="fa-solid fa-circle-check"></i> Tugallandi
        </button>
      `}
    </div>
  `;

  modal.classList.remove('hidden');
};

window.selectLesson = function(idx) {
  triggerHaptic('light');
  if (!appState.activeCourse) return;
  appState.activeLessonIndex = idx;
  const lesson = appState.activeCourse.syllabus[idx];
  const videoTitle = document.getElementById('videoLessonTitle');
  if (videoTitle) videoTitle.textContent = lesson.title;

  document.querySelectorAll('.lesson-item').forEach((item, i) => {
    item.classList.toggle('active', i === idx);
  });
  showToast(`Dars tanlandi: ${lesson.title}`);
};

window.playLessonVideo = function() {
  triggerHaptic('medium');
  showToast("🎬 Video dars yuklanmoqda...");
};

window.enrollCourse = function(courseId) {
  triggerHaptic('medium');
  if (!appState.enrolledCourses.includes(courseId)) {
    appState.enrolledCourses.push(courseId);
    localStorage.setItem('edu_enrolled', JSON.stringify(appState.enrolledCourses));
  }
  showToast("🎉 Kursga muvaffaqiyatli a'zo bo'ldingiz!");
  renderCourses();
  openCourseModal(courseId);

  // Telegram botga xabar uzatish
  if (tg) {
    tg.sendData(JSON.stringify({
      action: 'enroll',
      course_id: courseId,
      user_id: appState.user.id
    }));
  }
};

window.markLessonComplete = function(courseId) {
  triggerHaptic('light');
  if (!appState.activeCourse) return;
  const lesson = appState.activeCourse.syllabus[appState.activeLessonIndex];
  if (!appState.completedLessons[courseId]) {
    appState.completedLessons[courseId] = [];
  }
  if (!appState.completedLessons[courseId].includes(lesson.id)) {
    appState.completedLessons[courseId].push(lesson.id);
    localStorage.setItem('edu_completed', JSON.stringify(appState.completedLessons));
    showToast(`✅ "${lesson.title}" darsi tugallandi!`);
    renderCourses();
    openCourseModal(courseId);
  }
};

// 6. Test / Viktorina (Quiz) tizimi
let quizState = {
  courseId: null,
  currentQuestion: 0,
  score: 0,
  selectedAnswers: []
};

window.openQuizModal = function(courseId) {
  triggerHaptic('medium');
  const course = COURSES.find(c => c.id === courseId);
  if (!course || !course.quiz || course.quiz.length === 0) {
    showToast("Ushbu kurs uchun test tez orada qo'shiladi!");
    return;
  }

  quizState = {
    courseId: courseId,
    currentQuestion: 0,
    score: 0,
    selectedAnswers: []
  };

  const modal = document.getElementById('quizModal');
  const quizTitle = document.getElementById('quizTitle');
  quizTitle.textContent = `${course.title} - Test`;

  renderQuizStep();
  modal.classList.remove('hidden');
};

function renderQuizStep() {
  const course = COURSES.find(c => c.id === quizState.courseId);
  const container = document.getElementById('quizContent');
  if (!course || !container) return;

  const total = course.quiz.length;
  const current = quizState.currentQuestion;

  if (current >= total) {
    // Test natijalari
    renderQuizResults(course);
    return;
  }

  const q = course.quiz[current];

  container.innerHTML = `
    <div class="quiz-step-card">
      <div class="quiz-progress-text">Savol: ${current + 1} / ${total}</div>
      <div class="quiz-question">${q.question}</div>
      <div class="quiz-options">
        ${q.options.map((opt, optIdx) => `
          <button class="quiz-opt-btn" onclick="selectQuizAnswer(${optIdx}, ${q.answer})">
            <span>${opt}</span>
            <i class="fa-regular fa-circle"></i>
          </button>
        `).join('')}
      </div>
    </div>
  `;
}

window.selectQuizAnswer = function(selectedIdx, correctIdx) {
  triggerHaptic('light');
  const isCorrect = selectedIdx === correctIdx;
  if (isCorrect) {
    quizState.score += 1;
    triggerHaptic('medium');
  }

  quizState.selectedAnswers.push({ selectedIdx, correctIdx, isCorrect });
  quizState.currentQuestion += 1;

  setTimeout(() => {
    renderQuizStep();
  }, 400);
};

function renderQuizResults(course) {
  const container = document.getElementById('quizContent');
  const total = course.quiz.length;
  const percent = Math.round((quizState.score / total) * 100);

  // Saqlash
  appState.quizScores[course.id] = percent;
  localStorage.setItem('edu_scores', JSON.stringify(appState.quizScores));

  container.innerHTML = `
    <div class="quiz-result">
      <div class="result-icon">
        <i class="fa-solid fa-trophy"></i>
      </div>
      <div class="result-score">${quizState.score} / ${total} (${percent}%)</div>
      <div class="result-message">
        ${percent >= 70 
          ? "Ajoyib natija! Siz testni a'lo darajada topshirdingiz va bilimingizni tasdiqladingiz!" 
          : "Yaxshi urinish! Natijani yanada yaxshilash uchun darslarni takroran ko'rib chiqing."}
      </div>

      <button class="btn-primary" style="width: 100%; margin-bottom: 12px;" onclick="sendResultToTelegram()">
        <i class="fa-brands fa-telegram"></i> Natijani Botga Yuborish
      </button>

      <button class="btn-secondary" style="width: 100%;" onclick="closeQuizModal()">
        Yopish
      </button>
    </div>
  `;
}

window.sendResultToTelegram = function() {
  triggerHaptic('medium');
  const course = COURSES.find(c => c.id === quizState.courseId);
  const payload = {
    action: 'quiz_completed',
    course_id: quizState.courseId,
    course_title: course?.title || 'Kurs',
    score: quizState.score,
    total: course?.quiz?.length || 0,
    user: appState.user
  };

  if (tg) {
    try {
      tg.sendData(JSON.stringify(payload));
      showToast("🚀 Natijangiz Telegram botga yuborildi!");
      setTimeout(() => {
        closeQuizModal();
      }, 1000);
    } catch (e) {
      showToast("Natija saqlandi!");
    }
  } else {
    showToast("Natija saqlandi! (Telegram ichida botga uzatiladi)");
  }
};

window.closeQuizModal = function() {
  document.getElementById('quizModal').classList.add('hidden');
};

// 7. Shaxsiy Profil Modali
function renderProfile() {
  const container = document.getElementById('profileContent');
  if (!container) return;

  const enrolledCount = appState.enrolledCourses.length;
  let totalLessonsDone = 0;
  Object.values(appState.completedLessons).forEach(arr => {
    totalLessonsDone += arr.length;
  });

  container.innerHTML = `
    <div class="profile-card">
      <div class="avatar-large">${appState.user.firstName.charAt(0).toUpperCase()}</div>
      <div>
        <div class="profile-name">${appState.user.firstName} ${appState.user.lastName}</div>
        <div class="profile-tag">${appState.user.username || "@o'quvchi"}</div>
      </div>
    </div>

    <h4 style="font-size: 1rem; font-weight: 700; margin-bottom: 12px;">Yutuqlar & Statistika</h4>
    <div class="achievements-grid">
      <div class="achievement-card">
        <i class="fa-solid fa-book-bookmark"></i>
        <div class="ach-title">${enrolledCount} ta Kurs</div>
        <div class="ach-desc">A'zo bo'lingan</div>
      </div>
      <div class="achievement-card">
        <i class="fa-solid fa-circle-check"></i>
        <div class="ach-title">${totalLessonsDone} ta Dars</div>
        <div class="ach-desc">O'rganib chiqildi</div>
      </div>
      <div class="achievement-card">
        <i class="fa-solid fa-award"></i>
        <div class="ach-title">Sertifikatlar</div>
        <div class="ach-desc">Tez kunda</div>
      </div>
      <div class="achievement-card">
        <i class="fa-solid fa-fire"></i>
        <div class="ach-title">Faollik</div>
        <div class="ach-desc">Har kuni bilim</div>
      </div>
    </div>

    <button class="btn-primary" style="width: 100%;" onclick="closeProfileModal()">
      Tushunarli
    </button>
  `;
}

function openProfileModal() {
  triggerHaptic('light');
  renderProfile();
  document.getElementById('profileModal').classList.remove('hidden');
}

window.closeProfileModal = function() {
  document.getElementById('profileModal').classList.add('hidden');
};

// 8. Toast Bildirishnoma
function showToast(msg) {
  const toast = document.getElementById('toast');
  const toastMsg = document.getElementById('toastMsg');
  if (!toast || !toastMsg) return;

  toastMsg.textContent = msg;
  toast.classList.remove('hidden');
  setTimeout(() => {
    toast.classList.add('hidden');
  }, 2800);
}

// 9. Mavzuni o'zgartirish (Dark / Light Mode)
function setTheme(theme) {
  appState.theme = theme;
  localStorage.setItem('edu_theme', theme);
  const icon = document.querySelector('#themeToggleBtn i');

  if (theme === 'dark') {
    document.body.classList.add('dark-mode');
    if (icon) icon.className = 'fa-solid fa-sun';
  } else {
    document.body.classList.remove('dark-mode');
    if (icon) icon.className = 'fa-solid fa-moon';
  }
}

// 10. Event Listenerlar va Ishga tushirish
document.addEventListener('DOMContentLoaded', () => {
  initTelegram();
  setTheme(appState.theme);
  renderCourses();

  // Mavzu tugmasi
  document.getElementById('themeToggleBtn')?.addEventListener('click', () => {
    triggerHaptic('light');
    setTheme(appState.theme === 'dark' ? 'light' : 'dark');
  });

  // Profil ochish
  document.getElementById('profileOpenBtn')?.addEventListener('click', openProfileModal);
  document.getElementById('closeProfileModalBtn')?.addEventListener('click', closeProfileModal);

  // Kurs modali yopish
  document.getElementById('closeCourseModalBtn')?.addEventListener('click', () => {
    triggerHaptic('light');
    document.getElementById('courseModal').classList.add('hidden');
  });

  // Test modali yopish
  document.getElementById('closeQuizModalBtn')?.addEventListener('click', () => {
    triggerHaptic('light');
    document.getElementById('quizModal').classList.add('hidden');
  });

  // Qidiruv
  const searchInput = document.getElementById('searchInput');
  searchInput?.addEventListener('input', (e) => {
    appState.searchQuery = e.target.value.trim();
    renderCourses();
  });

  // Toifalar (Kategoriya filtrlari)
  const catButtons = document.querySelectorAll('.cat-pill');
  catButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      triggerHaptic('light');
      catButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      appState.currentCategory = btn.getAttribute('data-category') || 'all';
      renderCourses();
    });
  });

  // Pastki navigatsiya
  const bottomNavItems = document.querySelectorAll('.bottom-nav .nav-item');
  bottomNavItems.forEach(item => {
    item.addEventListener('click', () => {
      triggerHaptic('light');
      bottomNavItems.forEach(b => b.classList.remove('active'));
      item.classList.add('active');

      const view = item.getAttribute('data-view');
      if (view === 'profile') {
        openProfileModal();
      } else if (view === 'quiz') {
        openQuizModal('tg-bot');
      } else if (view === 'my-learning') {
        openProfileModal();
      } else {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    });
  });
});
