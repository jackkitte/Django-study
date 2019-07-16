from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.loader import get_template
from hashlib import sha256

from .mail import send_mail
from .forms import UserForm


def index(request):

    return render(request, 'index.html')

def login_view(request):

    if request.method != 'POST':
        return redirect('/')

    user = authenticate(
        request,
        username=request.POST.get('username'),
        password=request.POST.get('password')
    )
    if user is None:
        return redirect('/accounts/login')
    else:
        login(request, user)
        return redirect('/')

def create_user(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if form.is_valid():
            token = sha256(('eqd131' + str(username.encode('utf-8')) + ": " + str(email.encode('utf-8'))).encode('utf-8')).hexdigest()
            email_html = get_template('email.html').render(
                {
                    'username': username,
                    'email': email,
                    'token': token
                }
            )
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                is_active=False
            )
            user.save()
            send_mail(email, '確認用メール', email_html)

            print("after send mail")

            return redirect('/accounts/login/')
        else:
            print("existed user information")
            return redirect('/create_user_view')


    return redirect('/create_user_view')

def check_mail(request):

    usename = request.GET.get('username')
    user = User.objects.get(username=usename)
    token = sha256(('eqd131' + str(user.username.encode('utf-8')) + ": " + str(user.email.encode('utf-8'))).encode('utf-8')).hexdigest()

    if token == request.GET.get('token'):
        user.is_active = True
        user.save()
        return redirect('/')
    else:
        return redirect('/?failed=true')

def create_user_view(request):

    form = UserForm()

    return render(request, 'create_user_view.html', {'form': form})

@login_required
def logout_view(request):

    logout(request)

    return redirect('/')