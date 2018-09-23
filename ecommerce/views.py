from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm


def home(request):

    context = {'title': 'Hello World!', 'content': 'just the content'}

    if request.user.is_authenticated:
        context['premium_content'] = "Premium for authenticated"

    return render(request, 'home.html', context=context)

def about(request):
    return render(request, 'about.html', {})

def contact(request):

    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "content": "Welcome to the contact page",
        "form": contact_form,
        "brand": "New Brand Name"
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, 'contact/view.html', context=context)

