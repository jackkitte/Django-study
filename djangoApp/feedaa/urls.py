from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('form', views.form),
    path('post', views.post),
    path('feedaas', views.feedaas),
    path('search', views.search),
    path('delete', views.delete),
    path('page_form', views.page_form),
    path('page_post', views.page_post),
]