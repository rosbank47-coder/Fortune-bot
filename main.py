import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7989282401:AAGCSDdo4EmecdmexTrSXNm2tHrhy6EpuvM"  # токен от @BotFather

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ================= Главное меню =================
menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/horoscope"), KeyboardButton(text="/fortune")],
        [KeyboardButton(text="/palm"), KeyboardButton(text="/tarot")],
        [KeyboardButton(text="/love"), KeyboardButton(text="/compatibility")],
        [KeyboardButton(text="/year"), KeyboardButton(text="/ask")]
    ],
    resize_keyboard=True
)

# ================= START =================
@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        "✨ Привет! Я бот-предсказатель.\n\n"
        "🔮 Бесплатные команды:\n"
        " • /horoscope – ежедневный гороскоп\n"
        " • /fortune – случайное предсказание\n"
        " • /ask – магический шар (задай вопрос)\n\n"
        "💎 Платные услуги (пока недоступны):\n"
        " • /palm – гадание по руке\n"
        " • /tarot – расклад карт Таро\n"
        " • /love – любовный гороскоп\n"
        " • /compatibility – совместимость\n"
        " • /year – годовой прогноз",
        reply_markup=menu_kb
    )

# ================= FREE SERVICES =================
@dp.message(Command("horoscope"))
async def horoscope_cmd(message: types.Message):
    horoscopes = [
        "Сегодня звёзды обещают новые возможности ✨",
        "Важное решение лучше отложить до завтра 🌙",
        "Время действовать – удача на твоей стороне 🚀",
        "Прояви терпение и тебя ждёт награда 🍀",
        "Сегодня стоит прислушаться к интуиции 🔮",
    ]
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Другой прогноз 🔄", callback_data="horoscope_again")]]
    )
    await message.answer(random.choice(horoscopes), reply_markup=kb)

@dp.callback_query(lambda c: c.data == "horoscope_again")
async def horoscope_again(callback: types.CallbackQuery):
    horoscopes = [
        "Улыбка и добрые слова откроют тебе дорогу 😊",
        "День благоприятен для общения и новых знакомств 👥",
        "Сконцентрируйся на здоровье и отдыхе 🧘",
        "Финансовые вопросы решатся благополучно 💰",
        "Вечером тебя ждёт приятный сюрприз 🎁"
    ]
    await callback.message.answer(random.choice(horoscopes))

# -------- Fortune
@dp.message(Command("fortune"))
async def fortune_cmd(message: types.Message):
    fortunes = [
        "Ты встретишь важного человека 👤",
        "Неожиданное событие изменит планы 📌",
        "Тебя ждёт приятный подарок 🎁",
        "Скоро осуществится заветное желание 🌠",
    ]
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Ещё предсказание 🔮", callback_data="fortune_again")]]
    )
    await message.answer(random.choice(fortunes), reply_markup=kb)

@dp.callback_query(lambda c: c.data == "fortune_again")
async def fortune_again(callback: types.CallbackQuery):
    fortunes = [
        "Сегодняшняя идея станет успешным проектом 💡",
        "Финансовый успех уже близко 💵",
        "Тебе улыбнётся судьба 🌈",
        "Используй шанс, который появится сегодня 🔑"
    ]
    await callback.message.answer(random.choice(fortunes))

# ================= PREMIUM (NOT AVAILABLE YET) =================
async def premium_unavailable(message: types.Message, service_name: str):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="🔓 Разблокировать (скоро)", callback_data="unlock_soon")]]
    )
    await message.answer(f"⚠️ Услуга «{service_name}» пока недоступна. 🔒\n\nСкоро появится возможность её подключить!", reply_markup=kb)

@dp.message(Command("palm"))
async def palm_service(message: types.Message):
    await premium_unavailable(message, "Гадание по руке")

@dp.message(Command("tarot"))
async def tarot_service(message: types.Message):
    await premium_unavailable(message, "Карты Таро")

@dp.message(Command("love"))
async def love_service(message: types.Message):
    await premium_unavailable(message, "Любовный гороскоп")

@dp.message(Command("compatibility"))
async def compatibility_service(message: types.Message):
    await premium_unavailable(message, "Совместимость")

@dp.message(Command("year"))
async def year_service(message: types.Message):
    await premium_unavailable(message, "Годовой прогноз")

@dp.callback_query(lambda c: c.data == "unlock_soon")
async def unlock_soon(callback: types.CallbackQuery):
    await callback.message.answer("💡 Эта функция скоро станет доступной!\nСледи за обновлениями 🔮")

# ================= YES / NO GAME =================
@dp.message(Command("ask"))
async def ask_cmd(message: types.Message):
    await message.answer("🎱 Задай мне любой вопрос, и я отвечу 'Да' или 'Нет'.")

@dp.message()
async def yes_no_game(message: types.Message):
    if message.text.startswith("/"):  # игнорируем команды
        return
    answers = [
        "✅ Да!",
        "❌ Нет!",
        "🤔 Возможно...",
        "✨ Всё в твоих руках!",
        "⚖️ Шансы равны.",
        "🌟 Лучше спроси позже.",
    ]
    await message.answer(random.choice(answers))

# ================= RUN =================
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
