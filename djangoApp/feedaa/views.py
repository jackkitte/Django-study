from django.shortcuts import render, redirect
from django.http import Http404
from .models import Feed, Page
from .forms import FeedForm, PageForm


def index(request):


    return render(request, 'feedaa_index.html')

def feedaas(request):

    feeds = Feed.objects.all()

    return render(request, 'feedaas.html', {'feeds': feeds})

def form(request):

    form = FeedForm()

    return render(request, 'feedaa_form.html', {'form': form})

def page_form(request):

    form = PageForm({'id': request.GET.get('id')})

    return render(request, 'feedaa_page_form.html', {'form': form})

def post(request):

    title = request.POST.get('title')
    description = request.POST.get('description')
    href = request.POST.get('href')

    if request.method != 'POST':
        return redirect(to="/feedaa/form")

    form = FeedForm(request.POST)

    if form.is_valid():
        feed = Feed.objects.create(
            title=title,
            description=description,
            href=href
        )
        feed.save()
        
        return redirect(to="/feedaa/feedaas")
    else:
        return redirect(to="/feedaa/form")

def page_post(request):

    title = request.POST.get('title')
    description = request.POST.get('description')
    href = request.POST.get('href')
    date_published = request.POST.get('date_published')
    if request.method == 'POST' and title and description and href and date_published:
        feed = Feed.objects.get(id=request.POST["id"])
        page = Page.objects.create(
            title=title,
            description=description,
            href=href,
            date_published=date_published,
            feed=feed
        )
        page.save()

        return redirect(to="/feedaa/feedaas")

def search(request):

    query = request.GET.get('q')
    print(query)

    try:
        feed = Feed.objects.get(title=request.GET["q"])
        #feeds = Feed.objects.filter(title__contains=query)

        return render(request, 'feedaa_result.html', {'feeds': [feed]})
    except Feed.DoesNotExist:
        raise Http404("フィードがありません")

def delete(request):
    
    if request.method == 'POST' and request.POST.get('id'):
        feed = Feed.objects.get(id=request.POST.get('id'))
        feed.delete()

        return redirect(to="/feedaa/feedaas")


