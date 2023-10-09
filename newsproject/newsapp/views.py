from newsapi import NewsApiClient
from django.shortcuts import render

def index(request):
    newsapi = NewsApiClient(api_key='8fb6d35aeacf403aabc15122edef890c')
    trending = newsapi.get_top_headlines(sources='bbc-news')

    news_articles = []
    for news in trending['articles']:
        news_article = {
            'headline': news['title'],
            'description': news['description'],
            'url': news['url'],
            'author': news['author'],
            'date': news['publishedAt'],
            'img': news['urlToImage']
        }
        news_articles.append(news_article)

    return render(request, 'index.html', context={'news_articles': news_articles})
