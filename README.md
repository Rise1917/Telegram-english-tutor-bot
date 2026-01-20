# Telegram Bot с Gemini AI / Telegram Bot with Gemini AI

[English](#english) | [Русский](#русский)

---

## English

Telegram bot for learning English powered by Google Gemini AI.

### Description

The bot acts as an energetic English mentor who helps students bridge the gap between theory and real proficiency through natural conversation.

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Rise1917/Telegram-english-tutor-bot.git
```

2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `config.txt` file and add your tokens:
```
TG_TOKEN=your_telegram_bot_token
GEMINI_KEY=your_gemini_api_key
```

### Usage

```bash
python Bot.py
```

### How to use

1. Find the bot in Telegram
2. Send `/start` command
3. Start chatting in English

### Features

- Adaptive language complexity based on user level
- Natural conversation without formal lists
- Gentle error corrections within conversation context
- Chat history preservation for each user

### Requirements

- Python 3.8+
- Telegram Bot Token (get from @BotFather)
- Google Gemini API key

---

## Русский

Телеграм-бот для изучения английского языка на базе Google Gemini AI.

### Описание

Бот работает как энергичный наставник английского языка, который помогает студентам преодолеть разрыв между теорией и реальным владением языком через естественное общение.

### Установка

1. Клонируйте репозиторий:
```bash
git clone <url-репозитория>
cd ТГ-бот
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# или
source venv/bin/activate  # Linux/Mac
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл `config.txt` и добавьте ваши токены:
```
TG_TOKEN=ваш_токен_телеграм_бота
GEMINI_KEY=ваш_ключ_gemini_api
```

### Запуск

```bash
python Bot.py
```

### Использование

1. Найдите бота в Telegram
2. Отправьте команду `/start`
3. Начните общение на английском языке

### Функции

- Адаптивная сложность языка под уровень пользователя
- Естественное общение без формальных списков
- Мягкие исправления ошибок в контексте разговора
- Сохранение истории чата для каждого пользователя

### Требования

- Python 3.8+
- Токен Telegram Bot (получить у @BotFather)
- API ключ Google Gemini