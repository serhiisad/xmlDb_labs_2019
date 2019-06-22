from telethon import TelegramClient
from dotenv import load_dotenv
import os
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

api_id = os.getenv("APP_API_ID")
api_hash = os.getenv("APP_API_HASH")

phone = os.getenv("PHONE")
username = os.getenv("USERNAME")

#creating client
client = TelegramClient('serhiisad', api_id, api_hash)
client.start()