from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import cache_page

from news.views import CreateNews, NewsDetail, UpdateNews

urlpatterns = [
    path('', include('news.urls')),
    path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('update_news/<int:pk>/', UpdateNews.as_view(), name='update_news'),
    path('admin/', admin.site.urls),
    path('create_news/', cache_page(3600)(CreateNews.as_view()),
         name='create_news'),
]
