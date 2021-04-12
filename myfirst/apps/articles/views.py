import cgi

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Article, Comment
from django.urls import reverse


def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена")

    latest_comments_list = a.comment_set.order_by('-id')[:10]
    print("request =", request)

    return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except Exception:
        raise Http404("Статья не найдена")
    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))


def leave_comment_2(request):
    print("data =====", request.POST)


    return render(request, 'articles/dynamic.html')


def dynamic(request):

    return render(request, 'articles/dynamic.html')


# def index(request):
#     return render(request, 'myfirst/templates/list.html')
