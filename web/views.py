from django.shortcuts import render
from .models import ContactForm
import telebot

def index(request):
    return render(request, 'html/index.html')

def contact_form(request):
    bot = telebot.TeleBot("1430788241:AAFb6wS1b6O2zwgGk6UtgOyo72ZGgw7R990", parse_mode=None)

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact = ContactForm(name=name, email=email, message=message)

        # Telegram Settings
        chat_id = '-274132481'
        tg_message = {
            f'Имя:  {name}\n'
            f'Email:  {email}\n'
            f'Сообщение:  {message}\n'
        }

        bot.send_message(chat_id, tg_message)

        contact.save()

        return render(request, 'html/success.html')
    else:
        return render(request, 'html/index.html')