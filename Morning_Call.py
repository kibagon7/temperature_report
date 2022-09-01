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

app = Flask(__name__)

LINE_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]
USER_ID_ISHIGURO = os.environ["USERID_ISHIGURO"]
USER_ID_KAWAMURA = os.environ["USERID_KAWAMURA"]
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

def main():
    pushText = TextSendMessage(text="体温報告をしてください")
    line_bot_api.push_message(USER_ID_ISHIGURO, messages=pushText)
    line_bot_api.push_message(USER_ID_KAWAMURA, messages=pushText)


if __name__ == "__main__":
    main()