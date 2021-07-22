from django.shortcuts import render

from .models import Article
# Create your views here.

def index(request): 
    articles = Article.objects.filter(active=True).order_by('-created_at')
    context = {
        'articles' : articles
    }
    return render(request, 'article/index.html', context)