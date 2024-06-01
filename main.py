import requests

TOKEN = "7030511458:AAHHTGapgMb5_b7YDvySnDts2OC-LwUkWyA"
CHAT_ID = "80088917"

# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
# print(requests.get(url).json())
message = "Hello from pycharm, How r u?"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
res = requests.get(url)
print(res)
