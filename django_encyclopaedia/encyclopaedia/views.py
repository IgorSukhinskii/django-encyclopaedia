# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from encyclopaedia.models import Article
from itertools import groupby
from collections import defaultdict
from encyclopaedia.forms import ArticleForm
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse_lazy

def index(request):
    def group_by_letter(article_list):
        # assuming article_list is sorted
        result = []
        r = groupby(article_list, key=lambda a: a.name[0])
        for k, v in r:
            result.append((k,list(v)))
        return result

    #разбиваем список на 4 примерно одинаковые части
    article_list = sorted(list(Article.objects.all()), key=lambda a: a.name)
    div = len(article_list)/4
    rem = len(article_list) - div*4
    mark1 = div + (rem>0 and 1 or 0)
    mark2 = mark1 + div + (rem>1 and 1 or 0)
    mark3 = mark2 + div + (rem>2 and 1 or 0)

    groups = map(group_by_letter, [
        article_list[0:mark1],
        article_list[mark1:mark2],
        article_list[mark2:mark3],
        article_list[mark3:],
        ])

    return render(request, 'encyclopaedia/index.html', {
        'groups' : groups,
        })

#class Section(ListView):
#    queryset = Article.objects.filter(name__startswith=letter)

def section(request, letter):
    q1 = Article.objects.filter(name__startswith=letter)

    return render(request, 'encyclopaedia/section.html', {
        'letter' : letter,
        'articles': Article.objects.filter(name__startswith=letter),
        })

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'encyclopaedia/article-detail.html'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'encyclopaedia/article-form.html'

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'encyclopaedia/article-form.html'

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('index')