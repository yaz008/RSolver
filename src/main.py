from bot import bot
from telebot.types import Message, File
from utils.download import download_photo
from utils.recognize import recognize
from utils.gpt.ask import ask_gpt
from json import loads
from time import sleep

@bot.message_handler(commands=['start'])
def on_start(message: Message) -> None:
    greeting: str = 'Welcome to <b>RSolver</b>!\n\n'
    greeting += 'Send a text/photo of a task you want to solve'
    bot.send_message(chat_id=message.from_user.id,
                     text=greeting,
                     parse_mode='HTML')
    
@bot.message_handler(content_types=['text'])
def on_text(message: Message) -> None:
    solution_msg: Message = bot.send_message(chat_id=message.from_user.id,
                                             text='Recognition...')
    unscrambled_tasks: str = message.text
    tasks: list[str] = loads(ask_gpt(template_name='jsonify',
                                     subs={ 'TASKS': unscrambled_tasks }))
    
    bot.edit_message_text(text=f'Solving: 0 of {len(tasks)}',
                          chat_id=message.from_user.id,
                          message_id=solution_msg.id)

    solution: str = ''
    for index, task in enumerate(tasks, start=1):
        code: str = ask_gpt(template_name='solve',
                            subs={
                                'CONTEXT': solution,
                                'TASK': task
                            })
        solution += f'# {index}\n{code}\n\n'
        bot.edit_message_text(text=f'Solving: {index} of {len(tasks)}',
                              chat_id=message.from_user.id,
                              message_id=solution_msg.id)
        sleep(1)

    bot.edit_message_text(text=f'```r\n{solution}\n```',
                          chat_id=message.from_user.id,
                          message_id=solution_msg.id)

@bot.message_handler(content_types=['photo'])
def on_photo(message: Message) -> None:
    solution_msg: Message = bot.send_message(chat_id=message.from_user.id,
                                             text='Recognition...')
    download_photo(message=message)
    raw_tasks: str = recognize()
    unscrambled_tasks: str = ask_gpt(template_name='unscramble',
                                     subs={ 'TASKS': raw_tasks })
    tasks: list[str] = loads(ask_gpt(template_name='jsonify',
                                     subs={ 'TASKS': unscrambled_tasks }))
    
    bot.edit_message_text(text=f'Solving: 0 of {len(tasks)}',
                          chat_id=message.from_user.id,
                          message_id=solution_msg.id)

    solution: str = ''
    for index, task in enumerate(tasks, start=1):
        code: str = ask_gpt(template_name='solve',
                            subs={
                                'CONTEXT': solution,
                                'TASK': task
                            })
        solution += f'# {index}\n{code}\n\n'
        bot.edit_message_text(text=f'Solving: {index} of {len(tasks)}',
                              chat_id=message.from_user.id,
                              message_id=solution_msg.id)
        sleep(1)

    bot.edit_message_text(text=f'```r\n{solution}\n```',
                          chat_id=message.from_user.id,
                          message_id=solution_msg.id)

if __name__ == '__main__':
    bot.infinity_polling()