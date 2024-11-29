import telebot

bot = telebot.TeleBot('8003827378:AAHBmGWjIW5nDOMCpkgHypbnEnPkVMYoBqI')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет. Я короче баню за маты. Добавь меня в свою группу. Кста я буду работать когда компьютер Камрона будет включен.")


swear = [
    "хуй", "пизда", "ебать", "ебал", "блять", "сука", "мразь", "мудак",
    "гондон", "чмо", "гнида", "сучка", "дрянь", "подонок", "пидор", "пидорас", "пидораска", "шлюха","еблан","динаху","иди нахуй","гандон","пенис","гей","лесбиянка","пошел нахуй","пошол нахуй","пошла нахуй","педик"
]


def swear_word_detect(message):
    for i in swear:
        if i in message.lower():
            return True
    return False


@bot.message_handler(func=lambda message: True)
def check_message(message):
    if swear_word_detect(message.text):
        bot.send_message(message.chat.id,
                         f"@{message.from_user.username}, э не матерись!")
        bot.delete_message(message.chat.id, message.message_id)
bot.polling()
