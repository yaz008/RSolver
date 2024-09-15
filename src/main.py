from bot import bot
from telebot.types import Message, File
from utils.download import download_photo

@bot.message_handler(commands=['start'])
def on_start(message: Message) -> None:
    bot.send_message(chat_id=message.from_user.id, text='Hello!')

@bot.message_handler(content_types=['photo'])
def on_photo(message: Message) -> None:
    download_photo(message=message)

if __name__ == '__main__':
    bot.infinity_polling()