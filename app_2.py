from email import message
import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)


line_bot_api = LineBotApi('uOP1EvlLuDPE3vMMnCCwTU+E4GZy77NZBm/La/eKbKB6QSQl6dCN/4Tl4QHuJv9uSmtzurhrfVbji0YmwgDvFuHTEWbcjWAsI+IaMVj3CmkTpMAiho1lszGlzxS/h7qsm1hLQxUn1zXC7GBuhxANIgdB04t89/1O/w1cDnyilFU=')
parser = WebhookParser('e2f34508be9bd35f9bfe7207c4cb49d1')


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)


    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle.message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,messages)
    )

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT,5000_'))
    app.run(host='0.0.0.0'.debug, port=port)