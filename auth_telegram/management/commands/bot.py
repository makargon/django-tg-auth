import os
import telebot

from django.core.management.base import BaseCommand
from django.conf import settings
from auth_telegram.models import TelegramUser


bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def start(message):
    chat_id = message.chat.id
    token = message.text.split()[1] if len(message.text.split()) > 1 else None

    if token is not None:
        try:
            # Обновление или создание пользователя
            user, _ = TelegramUser.objects.update_or_create(chat_id=chat_id, defaults={
                'token': token, # Последний токен, с которым можно войти
                'username': message.from_user.username,
                'first_name': message.from_user.first_name,
                'last_name': message.from_user.last_name,
            })
            
            bot.send_message(
                chat_id=chat_id,
                text=f"Вход выполнен успешно"
            )
        except Exception as e:
            print(f'Ошибка при обработке сообщения: {e}')
            bot.send_message(
                chat_id=chat_id,
                text="Произошла ошибка при попытке входа. Попробуйте еще раз."
            )
    else:
        bot.send_message(
            chat_id=chat_id,
            text="Для того, что-бы войти в аккаунт перейдите по ссылке на сайте"
        )

# Добавление в manage.py
class Command(BaseCommand):
    help = 'Telegram Auth Bot'

    def handle(self, *args, **options):        
        bot.infinity_polling()