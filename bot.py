import telebot
from telebot import types

TOKEN = "7902109259:AAHkRGPFIkxrRrsph59QopPbXvJWDKVcigU"
bot = telebot.TeleBot(TOKEN)
WEB_APP_URL = "https://stanislav-backend.github.io/python-learning-app/"


@bot.message_handler(commands=["start"])
def send_welcome(message):
    # Создаем inline-кнопку
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(
        text="🚀 Запустить мини-приложение", web_app=types.WebAppInfo(url=WEB_APP_URL)
    )
    markup.add(btn)

    try:
        # Открываем локальный файл с картинкой
        with open("2.jpg", "rb") as photo:
            bot.send_photo(
                chat_id=message.chat.id,
                photo=photo,
                caption="🐍 *Добро пожаловать в «Путь Питониста»!*\n\n"
                "Интерактивный курс по Python прямо в Telegram!\n"
                "Нажмите кнопку ниже, чтобы начать обучение:",
                parse_mode="Markdown",
                reply_markup=markup,
            )
    except FileNotFoundError:
        # Если картинка не найдена, отправляем текст
        bot.send_message(
            chat_id=message.chat.id,
            text="🐍 *Добро пожаловать в «Путь Питониста»!*\n\n"
            "Интерактивный курс по Python прямо в Telegram!\n"
            "Нажмите кнопку ниже, чтобы начать обучение:",
            parse_mode="Markdown",
            reply_markup=markup,
        )


if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling()
