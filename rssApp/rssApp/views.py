from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.http import HttpResponseServerError

import feedparser
import logging
from hashlib import sha256

from .mail import send_mail
from .models import Feed, Page
from .forms import UserForm


logger = logging.getLogger(__name__)

def index(request):
    pages = Page.objects.all()
    return render(request, 'index.html', {'pages': pages})

def post(request):
    if request.method != 'POST':
        return redirect("/")
    try:
        rss = feedparser.parse(request.POST.get('url'))
        print(rss)
    except Exception:
        return redirect("/")
    if rss.entries:
        try:
            feed = Feed.objects.create(
                title=rss.feed.title,
                description=rss.feed.subtitle,
                href=request.POST.get('url')
            )
            feed.save()
            return redirect("/")
        except Exception:
            raise HttpResponseServerError()
    return redirect("/")

def login_view(request):
    # if request.method != 'POST':
    #     return redirect("/")

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is None:
        return redirect("/accounts/login")
    else:
        login(request, user)
        return redirect("/")

def create_user_view(request):
    form = UserForm()
    return render(request, 'create_user_view.html', {'form': form})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            token = sha256(('eqd131' + str(username.encode('utf-8')) + ": " + str(email.encode('utf-8'))).encode('utf-8')).hexdigest()
            email_html = get_template("email.html").render({
                'username': username,
                'email': email,
                'token': token
            })
            user = User.objects.create_user(
                username=username,
                email=email,
                password=request.POST.get('password'),
                is_active=False
            )
            user.save()
            send_mail(email, "確認用メール", email_html)
            return redirect("/accounts/login")
        else:
            print("無効なデータが含まれています")
            raise
    return redirect("/create_user_view")

def check_mail(request):
    request_username = request.GET.get('username')
    request_token = request.GET.get('token')
    user = User.objects.get(username=request_username)

    stored_username = user.username
    stored_email = user.email
    token = sha256(('eqd131' + str(stored_username.encode('utf-8')) + ": " + str(stored_email.encode('utf-8'))).encode('utf-8')).hexdigest()

    if token == request_token:
        user.is_active = True
        user.save()
        return redirect("/")
    else:
        return redirect("/?failed=true")

@login_required
def logout_view(request):
    logout(request)
    return redirect("/")