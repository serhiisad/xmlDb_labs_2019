import npyscreen
import filter
import asyncio
from database import database
from telethon import *

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

api_id = os.getenv("APP_API_ID")
api_hash = os.getenv("APP_API_HASH")
phone_number = os.getenv("PHONE")
#
# api_id="622138"
# api_hash="0fe897cfee15a26f5254fe01b3e42ed7"
# phone_number="+380971095129"

#
# api_id = os.getenv("APP_API_ID")
# api_hash = os.getenv("APP_API_HASH")
# phone_number = os.getenv("APP_PHONE")

# print("api_id : ", api_id)
# print("api_hash : ", api_hash)
# print("phone_number : ", phone_number)

session = 'serhiisad'
message_limit = 50000


db = database.connect()
class Parse(npyscreen.ActionForm):

    def create(self):
        self.value = None
        self.channel = self.add(npyscreen.TitleText, name="Channel:", value="")

    def beforeEditing(self):
        self.name = "Parse channel"

    def on_ok(self):
        if self.channel.value == '':
            npyscreen.notify_confirm("channel is empty", title='Info box')
        else:
            filter.remove_channel(self.channel.value)
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.get_messages(self.channel.value))

            self.parentApp.switchForm("MAIN")

    def on_cancel(self):
        self.parentApp.switchFormPrevious()

    def exit(self, *args, **keywords):
        self.parentApp.switchFormPrevious()

    async def get_messages(self, channel_name):
        client = TelegramClient(session, api_id, api_hash)
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone_number)
            me = client.sign_in(phone_number, input('Enter code: '))

        count = 0
        npyscreen.notify('Parsing...', title='Wait...')
        for post in client.iter_messages(channel_name, wait_time=0, limit=message_limit):
            count += 1

            if post.date is not None and post.message is not None and post.views is not None:

                result = {
                    "date": post.date,
                    "message": post.message.strip(),
                    "views": post.views,
                    "id": post.id,
                    "channel": channel_name
                }

                if (post.media):
                    result["media"] = False
                else:
                    result["media"] = True

                db["messages"].insert_one(result)
        print(f"parsed {count} messages from {channel_name}")
