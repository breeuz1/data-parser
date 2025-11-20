import telebot
import json

user_data = {}

with open("data-parser/config.json", "r") as f:
    config = json.load(f)

bot = telebot.TeleBot(config["telegram_token"])


@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(
        message.chat.id,
        "Привет, это новостной бот Habr. Напиши что тебе нужно. Можешь воспользоваться командой /help",
    )


@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.send_message(
        message.chat.id, "Привет, это актуавльный список команд:\n - /survey \n - /news"
    )


@bot.message_handler(content_types=["text"])
def echo(message):
    if message.text.startswith('/'):
        return
    bot.send_message(message.chat.id, f"Вы отпраили мне текст: '{message.text}'")


@bot.message_handler(commands=["survey"])
def start_survey(message):
    user_id = message.from_user.id

    if user_id not in user_data:
        user_data[user_id] = {}

    msg = bot.send_message(message.chat.id, "Как тебя зовут?")
    bot.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
    user_id = message.from_user.id
    user_data[user_id]["name"] = message.text

    msg = bot.send_message(message.chat.id, f"Приятно познакомиться! Сколько тебе лет?")
    bot.register_next_step_handler(msg, process_age_step)


def process_age_step(message):
    user_id = message.from_user.id

    try:
        age = int(message.text)
        user_data[user_id]["age"] = age

        user_info = user_data[user_id]

        bot.send_message(
            message.chat.id,
            f"Супер! Тебя зовут {user_info.get('name')}, тебе {user_info.get('age')} лет.",
        )
    except ValueError:
        bot.send_message(
            message.chat.id, "Возраст должен быть числом! Начни заново: /survey"
        )


print("Бот запущен!!!")

bot.polling(non_stop=True)
