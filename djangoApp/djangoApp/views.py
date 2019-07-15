from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from hashlib import md5

def index(request):

    return render(request, 'index.html', {'title': 'タイトル', 'message': 'メッセージ'})

def hoge(request):

    return HttpResponse("Hoge")

def fuga(request, foo):

    return render(request, 'index.html', {'title': foo})

def search(request):

    q = request.GET.get('q')
    return HttpResponse(q)

def render_form(request):

    return render(request, 'login.html')

def login(request):

    if request.POST['username'] and request.POST['email']:
        return render(request, 'check.html', {"email": request.POST['email'], "username": request.POST['username']})
    else:
        return render(request, 'error.html')

def form(request):

    return render(request, 'form.html')

def upload(request):

    file_image = request.FILES.get('image')
    name = request.POST['name']
    if request.method == 'POST' and file_image and (file_image.content_type == "image/png" or file_image.content_type == "image/jpeg"):
        extention = ".jpg"
        if file_image.content_type == "image/png":
            extention = ".png"
        print(file_image.name)
        filepath = 'static/' + md5(file_image.name.encode('utf-8')).hexdigest() + extention
        binary = request.FILES['image']
        with open(filepath, 'wb') as f:
            for chunk in binary.chunks():
                f.write(chunk)

        return render(request, 'result.html', {'filepath': filepath, 'name': name})
    else:
        return HttpResponseRedirect("/form")
