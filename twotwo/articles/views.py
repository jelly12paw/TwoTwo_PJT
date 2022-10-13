from django.shortcuts import render, redirect
from articles.forms import ArticleForm
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
    
def update(request, pk):
    articles = Article.objects.get(pk=pk)
    if request.method == "POST":
        article_form = ArticleForm(request.POST, instance=articles)
        if article_form.is_valid():
            article_form.save()
            return redirect("accounts:index")
    else:
        article_form = ArticleForm(instance=articles)
    context = {
        "article_form": article_form,
        "articles": articles,
    }
    return render(request, 'articles/update.html', context)