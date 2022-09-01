from flask import Flask, request, abort
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import Scraping_time

app = Flask(__name__)

LINE_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]
USER_ID_ISHIGURO = os.environ["USERID_ISHIGURO"]
USER_ID_KAWAMURA = os.environ["USERID_KAWAMURA"]
LOGINID_ISHIGURO = os.environ["LOGINID_ISHIGURO"]
LOGINID_KAWAMURA = os.environ["LOGINID_KAWAMURA"]
PASSWORD_ISHIGURO = os.environ["PASSWORD_ISHIGURO"]
PASSWORD_KAWAMURA = os.environ["PASSWORD_KAWAMURA"]
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

def main():
    if Scraping_time.report_time(LOGINID_KAWAMURA, PASSWORD_KAWAMURA) == 0:
        pushText = TextSendMessage(text="体温報告がまだ完了していません")
        line_bot_api.push_message(USER_ID_KAWAMURA, messages=pushText)

    if Scraping_time.report_time(LOGINID_ISHIGURO, PASSWORD_ISHIGURO) == 0:
        pushText = TextSendMessage(text="体温報告がまだ完了していません")
        line_bot_api.push_message(USER_ID_ISHIGURO, messages=pushText)
    


if __name__ == "__main__":
    main()