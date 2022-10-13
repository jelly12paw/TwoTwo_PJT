from django.shortcuts import redirect, render
from articles.forms import ArticleForm
from .models import Article

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