import os
import requests
import random

BOT_TOKEN = os.environ['BOT_TOKEN']
BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'

CHAT_ID_2 = os.environ['CHAT_ID_2']

# List of file paths to send
file_paths = ['Hy2F.txt', 'HysteriaF.txt', 'SsF.txt', 'SsrF.txt', 'TrojanF.txt', 'TuicF.txt', 'VlessF.txt', 'VmessF.txt', 'socksF.txt', 'mtprotoF.txt', 'juicityF.txt']

# Send each file
for file_path in file_paths:
    # Open the file
    with open(file_path, 'rb') as file:
        # Prepare the file for sending
        file_data = {'document': file}
        message_payload = {
            'chat_id': CHAT_ID_2,
            'caption': f'File: {file_path}',
        }

        # Send the file
        response = requests.post(BASE_URL + 'sendDocument', data=message_payload, files=file_data)

        if response.status_code == 200:
            print(f'Successfully sent file {file_path} to channel!')
        else:
            print(f'Failed to send file {file_path} to channel.')
            print(f'Response status code: {response.status_code}')
            print(f'Response text: {response.text}')
