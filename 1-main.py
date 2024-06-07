import requests

# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values
# loading variables from .env file
load_dotenv()

# accessing and printing value
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json())
# message = "Hello I am your TeleBot, Nice to meet you :-)"
# url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
# res = requests.get(url)
# print(res)
