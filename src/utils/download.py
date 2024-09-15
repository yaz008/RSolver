from bot import bot
from telebot.types import Message, File

def download_photo(message: Message) -> None:
    file_id: str = message.photo[-1].file_id
    file_info: File = bot.get_file(file_id)
    photo: bytes = bot.download_file(file_info.file_path)
    with open(file=f'temp.png', mode='wb') as photo_file:
        photo_file.write(photo)