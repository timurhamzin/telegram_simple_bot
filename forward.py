import os
import telegram
from dotenv import load_dotenv

from telegram.ext import Updater, Filters, MessageHandler

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
proxy = telegram.utils.request.Request(
    proxy_url='socks5://109.194.175.135:9050')
bot = telegram.Bot(token=TELEGRAM_TOKEN, request=proxy)
updater = Updater(token=TELEGRAM_TOKEN)


def send_message(message):
    return bot.send_message(chat_id=CHAT_ID, text=message)


def forward(update, context):
    context.bot.forward_message(CHAT_ID, update.message.chat.id,
                                update.message.message_id)
    # update.message.reply_text('Привет, я бот')


if __name__ == '__main__':
    updater.dispatcher.add_handler(MessageHandler(Filters.text, forward))
    updater.start_polling()
    updater.idle()
