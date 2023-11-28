import telebot

bot = telebot.TeleBot('6725254847:AAGvtYoD8xUrk5xHsXcf2lnTKfEaLxMOKOw')

@bot.message_handler(commands=['Привет'])
def main(message):
    bot.send_message(message.chat.id, '*Привет!* Рада пообщаться!', parse_mode='Markdown')


@bot.message_handler(commands=['Скинь фото'])
def main(message):
    bot.send_message(message.chat.id, 'Лучше почитай! [ссылка](https://habr.com/ru/companies/piter/articles/540346/)',
                     parse_mode='Markdown')


@bot.message_handler(commands=['Пока'])
def main(message):
    bot.send_message(message.chat.id, 'Пока! Ещё увидимся!', parse_mode='Markdown')


bot.infinity_polling()