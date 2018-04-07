from django.shortcuts import render, HttpResponse,get_object_or_404
from .models import Article
from django.template import loader

# Create your views here.
def index(request):
    blog_list = Article.objects.order_by('-update_time')
    context = {'website_title': 'simple_blog','blog_list':blog_list}
    return render(request, 'index.html', context)

def article(request, article_id):
    # article = Article.objects.get(pk=article_id)
    article = get_object_or_404(Article, pk=article_id)
    context = {'website_title': 'simple_blog', 'article': article}
    return render(request, 'article.html', context)
