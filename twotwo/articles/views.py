from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')

    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):

    article = Article.objects.get(id=pk)

    context = {
        'article': article
    }
    
    return render(request, 'articles/detail.html', context)