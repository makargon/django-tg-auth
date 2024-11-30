import uuid
from django.shortcuts import render
from django.contrib.auth import login
from django.conf import settings

from .models import TelegramUser


def index(request):
    token = request.COOKIES.get('token')
    context = {}
    if token is None:
        token = str(uuid.uuid4())
    else:
        user = TelegramUser.objects.filter(token=token).first()
        if user:
            login(request, user)

    context['token'] = token  # Для генерации ссылки 
    context['TELEGRAM_BOT_USERNAME'] = settings.TELEGRAM_BOT_USERNAME  # Для генерации ссылки

    response = render(request, 'auth.html', context)
    response.set_cookie('token', token, max_age=60*60*12)  # Ставим куки на 12 часов
    return response
