from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('all_news', views.all_news, name='anews'),
    path('game_news', views.game_news, name='game'),
    path('news', views.news, name='news_us'),
]
