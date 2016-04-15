from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^news$', views.news, name='news'),
    url(r'^cats$', views.cats, name='cats'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^forum$', views.forum, name='forum'),
    url(r'^contacts$', views.contacts, name='contacts'),
]