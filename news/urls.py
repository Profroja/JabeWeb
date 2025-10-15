from django.urls import path
from . import views

urlpatterns = [
    path('news-list/', views.news_list, name='news-list'),
    path('news-detail/<int:news_id>/', views.news_detail, name='news-detail'),
]
