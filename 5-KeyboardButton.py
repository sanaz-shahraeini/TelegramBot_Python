# added regular Keyboard Buttons (not inline) to the bot.
# This will provide users with a set of options they can tap on,
#  which will appear as part of the chat interface.

"""
Customizing the Buttons:
Add more buttons by creating additional KeyboardButton instances and adding them to the markup.
Modify the responses in the handlers to suit your bot’s functionality.

added regular Keyboard Buttons (not inline) to the bot.
This will provide users with a set of options they can tap on,
 which will appear as part of the chat interface.
"""

import telebot
import sqlite3
from telebot import types
import os
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
        bot.reply_to(message, "Welcome, new user! Use the buttons below to navigate.", reply_markup=get_main_menu())
    else:
        bot.reply_to(message, "Welcome back! Use the buttons below to navigate.", reply_markup=get_main_menu())


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "How can I assist you?", reply_markup=get_main_menu())


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text, reply_markup=get_main_menu())


def get_main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton("Option 1")
    btn2 = types.KeyboardButton("Option 2")
    btn3 = types.KeyboardButton("Option 3")
    markup.add(btn1, btn2, btn3)
    return markup


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "button1":
        bot.answer_callback_query(call.id, "Button 1 clicked!")
        bot.send_message(call.message.chat.id, "You clicked Button 1!", reply_markup=get_main_menu())
    elif call.data == "button2":
        bot.answer_callback_query(call.id, "Button 2 clicked!")
        bot.send_message(call.message.chat.id, "You clicked Button 2!", reply_markup=get_main_menu())


if __name__ == '__main__':
    init_db()
    bot.infinity_polling()
