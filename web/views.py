from django.shortcuts import render
from .models import ContactForm

def index(request):
    return render(request, 'html/index.html')

def contact_form(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact = ContactForm(name=name, email=email, message=message)
        contact.save()

        return render(request, 'html/success.html')
    else:
        return render(request, 'html/index.html')