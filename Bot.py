import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import google.generativeai as genai

# --- НАСТРОЙКИ ---
def load_config():
    config = {}
    with open('config.txt', 'r') as f:
        for line in f:
            key, value = line.strip().split('=', 1)
            config[key] = value
    return config

config = load_config()
TG_TOKEN = config['TG_TOKEN']
GEMINI_KEY = config['GEMINI_KEY']
prompt = "You are an energetic English mentor and supportive partner who helps students bridge the gap between theory and real proficiency by providing natural, human-like conversation without any unnecessary symbols like asterisks. You must seamlessly adapt your language complexity to the user's current level, focusing on genuine interaction and cultural nuances while subtly weaving corrections into your responses instead of using harsh criticism or formal lists."
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel(model_name='gemini-2.5-flash-lite',
                              system_instruction=(
                                  prompt
                              )) # Быстрая и бесплатная модель
user_chats = {}
bot = Bot(token=TG_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    user_chats[message.from_user.id] = model.start_chat(history=[])
    await message.answer("Привет! Я бот на базе Gemini. Спрашивай что угодно.")

@dp.message()
async def chat_handler(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    
    user_id = message.from_user.id
    
    if user_id not in user_chats:
        user_chats[user_id] = model.start_chat(history=[])
    
    chat = user_chats[user_id]
    
    try:
        response = await asyncio.to_thread(chat.send_message, message.text)
        await message.reply(response.text)
    except Exception as e:
        await message.reply("Error. Try /start to reset.")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())