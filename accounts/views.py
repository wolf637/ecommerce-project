from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, GuestForm
from django.contrib.auth import authenticate, login, get_user_model
from django.utils.http import is_safe_url
from .models import GuestEmail

def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
        "form": form
    }

    next_get = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_get or next_post or None

    if form.is_valid():
        email = form.cleaned_data.get('email')
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/register/")

    return redirect("/register/")

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }

    next_get = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_get or next_post or None

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            context['form'] = LoginForm()
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        else:
            print("Login error")
    return render(request, "accounts/login.html", context=context)

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
    return render(request, "accounts/register.html", context=context)