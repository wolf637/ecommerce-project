from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, LoginForm, RegisterForm


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


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("Authenticated: {}".format(request.user.is_authenticated()))
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print("Authenticated: {}".format(request.user.is_authenticated()))
        if user is not None:
            print("Authenticated after if: {}".format(request.user.is_authenticated()))
            login(request, user)
            context['form'] = LoginForm()
            return redirect("/")
        else:
            print("Login error")
    return render(request, "auth/login.html", context=context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {"form": form }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        new_user = User.objects.create_user(username=username, password=password, email=email)
        print(new_user)
    return render(request, "auth/register.html", context=context)