from django.shortcuts import render, get_object_or_404
from .models import News

def news_list(request):
    news_articles = News.objects.all()
    context = {
        'news_articles': news_articles
    }
    return render(request, 'news-list.html', context)

def news_detail(request, news_id):
    news_article = get_object_or_404(News, id=news_id)
    context = {
        'news_article': news_article
    }
    return render(request, 'news-detail.html', context)