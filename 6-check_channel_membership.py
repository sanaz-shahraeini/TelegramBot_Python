# allow users to interact with it only if they have joined specific Telegram channels.
# We will use the get_chat_member method to check if the user is a member of the required channels.
"""
Database Initialization:

init_db(): Initializes the SQLite database and creates the users table if it doesn't exist.
Check User Function:

is_new_user(user_id): Checks if a user is new or returning by querying the users table. Adds new users to the table.
Membership Check Function:

is_member_of_required_channels(user_id): Checks if the user is a member of the required channels. It uses the get_chat_member method to verify the membership status.
Bot Handlers:

/start command: Greets users if they are members of the required channels; otherwise, asks them to join the channels.
/help command and message handler: Provides help options and handles messages only if the user is a member of the required channels.
get_main_menu(): Creates a Reply Keyboard with three buttons.
handle_query(call): Handles button clicks and responds accordingly.
Customizing the Buttons:
Add more buttons by creating additional KeyboardButton instances and adding them to the markup.
Modify the responses in the handlers to suit your bot’s functionality.
"""

"""
Important Notes:
1- Ensure that your bot has the necessary permissions to check membership status in the channels.
2- The bot must be an administrator in the channels it is checking, or the channels must be public.
"""

import telebot
import sqlite3
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
# CHAT_ID = os.getenv("CHAT_ID")

bot = telebot.TeleBot(token=TOKEN)

# List of required channel usernames
# REQUIRED_CHANNELS = os.getenv("REQUIRED_CHANNELS")
REQUIRED_CHANNELS = ['@Ostad7.com']

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


# Check if user is a member of the required channels
def is_member_of_required_channels(user_id):
    for channel in REQUIRED_CHANNELS:
        try:
            member = bot.get_chat_member(chat_id=channel, user_id=user_id)
            if member.status not in ['member', 'administrator', 'creator']:
                return False
        except telebot.apihelper.ApiException as e:
            print(f"Error checking membership status for user {user_id} in channel {channel}: {e}")
    return True


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if is_member_of_required_channels(user_id):
        if is_new_user(user_id):
            bot.reply_to(message, "Welcome, new user! Use the buttons below to navigate.", reply_markup=get_main_menu())
        else:
            bot.reply_to(message, "Welcome back! Use the buttons below to navigate.", reply_markup=get_main_menu())
    else:
        bot.reply_to(message, "You need to join the required channels to use this bot https://t.me/+Q7b_SxWyNcl34Eud")


@bot.message_handler(commands=['help'])
def send_help(message):
    user_id = message.from_user.id
    if is_member_of_required_channels(user_id):
        bot.reply_to(message, "How can I assist you?", reply_markup=get_main_menu())
    else:
        bot.reply_to(message, "You need to join the required channels to use this bot.")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user_id = message.from_user.id
    if is_member_of_required_channels(user_id):
        bot.reply_to(message, message.text, reply_markup=get_main_menu())
    else:
        bot.reply_to(message, "You need to join the required channels to use this bot.")


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
