#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('+DfJ4rR25xnQ38akLCMmxMImZlUTemztz9vGbECAQxR7u42DWwGYmNpGmg1XgHoaIZhZnsjcVD63PnmbdbnGn6gFP8rfauqzq2cq9Zm8lVa81h3buRNywH/Sc9QY4VVW7cGc8WusCp2/AwMYeZyuCwdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('33c917c1288598e922e0cd904f305024')

line_bot_api.push_message('Ua564bc1573bcfe856f1a144363692b45', TextSendMessage(text='想去什麼縣市'))

# 監聽所有來自 /callback 的 Post Request
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
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    line_bot_api.reply_message(event.reply_token,TextSendMessage('gua'))

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
