from bot import bot
from telebot.types import Message, File
from utils.download import download_photo
from utils.recognize import recognize
from utils.gpt.ask import ask_gpt
from json import loads

@bot.message_handler(commands=['start'])
def on_start(message: Message) -> None:
    bot.send_message(chat_id=message.from_user.id, text='Hello!')

@bot.message_handler(content_types=['photo'])
def on_photo(message: Message) -> None:
    download_photo(message=message)
    raw_tasks: str = recognize()
    unscrambled_tasks: str = ask_gpt(template_name='unscramble',
                                     subs={ 'TASKS': raw_tasks })
    tasks: list[str] = loads(ask_gpt(template_name='jsonify',
                                     subs={ 'TASKS': unscrambled_tasks }))
    bot.send_message(chat_id=message.from_user.id,
                     text=str(tasks))

if __name__ == '__main__':
    bot.infinity_polling()