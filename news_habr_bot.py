import telebot


import json

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
        message.chat.id, "Привет, это актуавльный список команд:\n - /news"
    )


@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, f"Вы отпраили мне текст: '{message.text}'")


print("Бот запущен!!!")

bot.polling(non_stop=True)
