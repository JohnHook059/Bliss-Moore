from django.shortcuts import render
from .models import Cat, Article


def index(request):
    return render(request, 'main.html')


def news(request):
    return render(request, 'news.html', {'args': Article.objects.all()})


def cats(request):
    return render(request, 'cats.html', {'args': Cat.objects.all()})


def gallery(request):
    return render(request, 'gallery.html')


def articles(request):
    return render(request, 'articles.html', {'args': Article.objects.all()})


def contacts(request):
    return render(request, 'contacts.html')
