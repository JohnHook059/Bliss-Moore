from django.shortcuts import render


def index(request):
    return render(request, 'main.html')

def news(request):
    return render(request, 'news.html')

def cats(request):
    return render(request, 'cats.html')

def gallery(request):
    return render(request, 'gallery.html')

def forum(request):
    return render(request, 'forum.html')

def contacts(request):
    return render(request, 'contacts.html')