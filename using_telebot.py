import telebot
# pip install pyTelegramBotAPI

# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values

# loading variables from .env file
load_dotenv()

# accessing and printing value
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the bot!")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "How can I assist you?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    bot.infinity_polling()

bot.infinity_polling()
