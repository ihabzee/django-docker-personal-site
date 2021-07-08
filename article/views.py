from django.shortcuts import render

from .models import Article
# Create your views here.

def index(request): 
    articles = Article.objects.filter(active=True)
    context = {
        'articles' : articles
    }
    return render(request, 'article/index.html', context)