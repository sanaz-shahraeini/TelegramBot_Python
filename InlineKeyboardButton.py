# added Inline Keyboard Buttons to Telegram bot. This will allow users to interact with the bot through buttons,
# enhancing the user experience.
"""
Database Initialization:

init_db(): Initializes the SQLite database and creates the users table if it doesn't exist.
Check User Function:

is_new_user(user_id): Checks if a user is new or returning by querying the users table. Adds new users to the table.
Inline Keyboards:

get_main_menu(): Creates an Inline Keyboard with two buttons.
send_welcome(message): Uses the Inline Keyboard to greet users.
send_help(message): Provides help options using the Inline Keyboard.
handle_query(call): Handles button clicks and responds accordingly.
Customizing the Buttons:
Add more buttons by creating additional InlineKeyboardButton instances and adding them to the markup.
Modify the callback data and responses in the handle_query function to suit your bot’s functionality.

"""
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
        bot.reply_to(message, "Welcome, new user! Click a button to proceed.", reply_markup=get_main_menu())
    else:
        bot.reply_to(message, "Welcome back! Click a button to proceed.", reply_markup=get_main_menu())


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "How can I assist you?", reply_markup=get_main_menu())


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


def get_main_menu():
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton(text="Button 1", callback_data="button1")
    btn2 = telebot.types.InlineKeyboardButton(text="Button 2", callback_data="button2")
    markup.add(btn1, btn2)
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
