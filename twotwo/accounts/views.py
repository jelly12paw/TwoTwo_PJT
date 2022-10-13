from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
@login_required
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else: 
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/form.html', context=context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
    'form': form,
    }
    return render(request, 'accounts/change_password.html', context)

@login_required
def delete(request, pk):
    articles = Article.objects.get(pk=pk)
    articles.delete()
    return redirect('articles:index')