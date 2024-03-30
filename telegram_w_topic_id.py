import requests
import time
from config import TG_TOKEN,CHAT_ID,TOPIC_MESSAGE_ID

def send_telegram_message(token, chat_id, message_text, topic_message_id):
    send_message_url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message_text,
        "reply_to_message_id": topic_message_id,
    }
    response = requests.post(send_message_url, data=data)
    return response.json()

#config.py file format     TG_TOKEN = 'ID_HERE'
bot_token = TG_TOKEN
chat_id = CHAT_ID
topic_message_id = TOPIC_MESSAGE_ID

# Path to a text file
file_path = '/alert.txt'

# Open the file and read line by line
with open(file_path, "r") as file:
    for line in file:
        # Check if line is not just a newline character
        if line.strip():
            response = send_telegram_message(bot_token, chat_id, line.strip(), topic_message_id)
            print(response)
            time.sleep(1)  # Pause for 1 second before sending the next line
