# 🤖 Telegram Bot with Python

This repository contains a Telegram bot built using Python and the `pyTelegramBotAPI` library. The bot includes features such as checking if a user is new, managing SQLite databases for user data, and ensuring users are members of specific channels before allowing them to interact with the bot.

## ✨ Features

- 📝 User registration check
- 🗄️ SQLite database integration
- ⌨️ Inline and reply keyboard buttons
- ✅ Channel membership verification

## 🛠️ Getting Started

### 📋 Prerequisites

- Python 3.x
- `pyTelegramBotAPI` library

### 📦 Installation

1. Clone the repository:

    ```bash
    git clone https://github.com//sanaz-shahraeini/TelegramBot_Python.git
    cd TelegramBot_Python
    ```

2. Install the required libraries:

    ```bash
    pip install pyTelegramBotAPI
    ```

### 🚀 Bot Setup

1. Replace `'YOUR_API_KEY_HERE'` in the code with your actual Telegram Bot API key.

2. Set the list of required channel usernames in the `REQUIRED_CHANNELS` variable.

### ▶️ Running the Bot

Run the bot using the following command:

```bash
python bot.py
