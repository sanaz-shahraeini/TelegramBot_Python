# Here's the full code for the bot using SQLite to check if a user is new or returning:
import telebot
import sqlite3
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv, dotenv_values

load_dotenv()
TOKEN = os.getenv("TOKEN")
# CHAT_ID = os.getenv("CHAT_ID")

bot = telebot.TeleBot(token=TOKEN)

# SQLite database file
DB_FILE = 'users.db'


# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY
                      )''')
    conn.commit()
    conn.close()


# Check if user is new and update the database
def is_new_user(user_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT user_id FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    if user is None:
        cursor.execute('INSERT INTO users (user_id) VALUES (?)', (user_id,))
        conn.commit()
        conn.close()
        return True
    conn.close()
    return False


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if is_new_user(user_id):
        bot.reply_to(message, "Welcome, new user!")
    else:
        bot.reply_to(message, "Welcome back!")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "How can I assist you?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    init_db()
    bot.infinity_polling()
