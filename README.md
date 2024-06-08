# 🤖 Telegram Bot with Python

This repository contains a Telegram bot built using Python and the `pyTelegramBotAPI` library. The bot includes features such as checking if a user is new, managing SQLite databases for user data, and ensuring users are members of specific channels before allowing them to interact with the bot.

## ✨ Features ( a step by step guid )

- ⚓ Connection between telegram bot & python program
- ⌨️ Inline and reply keyboard buttons
- 🗄️ SQLite database integration
- 📝 User registration check
- ✅ Channel membership verification

## 🛠️ Getting Started

### 📋 Prerequisites

- Python 3.x
- `pyTelegramBotAPI` library
- `python-dotenv` library

### 📦 Installation

1. Clone the repository:
    ```bash
    git clone https://github.com//sanaz-shahraeini/TelegramBot_Python.git
    cd TelegramBot_Python
    ```

3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

### 🚀 Bot Setup

1.  Create a .env File 📝
   
 <p>Create a file named .env in the root directory of your project and add your Telegram bot token to it:</p>
   ```bash
    TOKEN = "YOUR BBOT API KEY"
  ```
3. Set the list of required channel usernames in the `REQUIRED_CHANNELS` variable if you wanna run 6-check_channel_membership.py file
   ```bash
   REQUIRED_CHANNELS = ['@channel_username1', '@channel_username2']
   ```


### ▶️ Running the Bot

Run the bot using the following command:
  ```bash
   python One_filename.py
  ```

### 📌Additional Notes 

- Ensure your bot has the necessary permissions to check membership status in the channels.
- The bot must be an administrator in the channels it is checking, or the channels must be public.
