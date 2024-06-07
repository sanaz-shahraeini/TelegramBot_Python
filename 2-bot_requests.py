import requests

TOKEN = "Your API Key"
CHAT_ID = "chat_id of a user"

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json())
#
# message = "sample message"
# url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
# res = requests.get(url)
# print(res)
