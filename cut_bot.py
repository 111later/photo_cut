import cut
import telebot
from pathlib import Path
from cfg import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в бот, загрузите фото для обработки!')


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    # download img
    src = '/home/ibragim/photo_cut/1_REMOVE_BACKGROUND/input_imgs/' + file_info.file_path
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Погнал воркать, ожидайте пару сек")
    # запуск скрипта rembg
    cut.remove_bg()


    list_of_extensions = ["*.png", "*.jpg"]
    all_files = []

    for ext in list_of_extensions:
        all_files.extend(Path("/home/ibragim/photo_cut/1_REMOVE_BACKGROUND/output_imgs/photos").glob(ext))

    for item in all_files:
        input_path = Path(item)
        file_name = input_path.stem
    bot.send_photo(message.chat.id, open(f'/home/ibragim/photo_cut/1_REMOVE_BACKGROUND/output_imgs/photos/{file_name}.png', 'rb'))


bot.polling(none_stop=True)
