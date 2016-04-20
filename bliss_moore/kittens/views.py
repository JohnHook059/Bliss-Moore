from django.shortcuts import render
from .models import Cat, Article


def index(request):
    return render(request, 'main.html')


def news(request):
    return render(request, 'news.html')


def cats(request):
    array_cats = Cat.objects.all()
    list_cats = []
    for cat in array_cats:
        cat_dict = {}
        cat_dict['name'] = cat.name
        cat_dict['color'] = cat.color
        cat_dict['male'] = cat.male
        cat_dict['breed'] = cat.breed
        cat_dict['birthday'] = cat.birthday
        cat_dict['father'] = cat.father
        cat_dict['mother'] = cat.mother
        cat_dict['kitten'] = cat.kitten
        cat_dict['litter'] = cat.litter
        cat_dict['status'] = cat.status
        list_cats.append(cat_dict)
    return render(request, 'cats.html', {'args': list_cats})


def gallery(request):
    return render(request, 'gallery.html')


def articles(request):
#    array_articles = Article.object.all()
#    list_articles = []
#    for article in array_articles:
#        list_articles.append([article.title, article.text])
#    return render(request, 'articles.html', {'args': list_articles})
    return render(request, 'articles.html', {'args': Article.objects.all()})


def contacts(request):
    return render(request, 'contacts.html')
