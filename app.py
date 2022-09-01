from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os
import Scraping


app = Flask(__name__)

YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/")
def hello():
    return "hello world"
    

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    profile = line_bot_api.get_profile(event.source.user_id)
    user_id = profile.user_id
    user_name = profile.display_name
    input_text = event.message.text
    
    if user_id == os.environ["USERID_ISHIGURO"]:    
        loginid = os.environ["LOGINID_ISHIGURO"]
        password = os.environ["PASSWORD_ISHIGURO"]
        
    elif user_id == os.environ["USERID_KAWAMURA"]:    
        loginid = os.environ["LOGINID_KAWAMURA"]
        password = os.environ["PASSWORD_KAWAMURA"]

    else:        
        if input_text == "登録":
            line_bot_api.push_message(os.environ["USERID_ISHIGURO"], TextSendMessage(text=user_name))
            line_bot_api.push_message(os.environ["USERID_ISHIGURO"], TextSendMessage(text=user_id))
            line_bot_api.push_message(user_id, TextSendMessage(text='登録を開始します。WebClassのIDとパスワードを間で改行して入力してください。'))
            return

        elif len(input_text) > 10:
            line_bot_api.push_message(os.environ["USERID_ISHIGURO"], TextSendMessage(text=input_text))
            line_bot_api.push_message(user_id, TextSendMessage(text='登録中です。完了次第連絡します。'))

            return
        
        else:
            line_bot_api.push_message(user_id, TextSendMessage(text='入力が正しくありません。'))  
            
            return
        
        
    line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text="体温報告を行います"))
    
    try:
        Scraping.report(loginid, password)
        line_bot_api.push_message(user_id, TextSendMessage(text='体温報告が完了しました'))
    
    except Exception as e:
        line_bot_api.push_message(user_id, TextSendMessage(text = str(e)))

        
        
if __name__ == "__main__":
    port = os.getenv("PORT") 
    app.run(host = "0.0.0.0", port = port)
    
    
    
    
    
    
    
    
    
    
    
    