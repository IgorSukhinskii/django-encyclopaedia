from django.http import HttpResponse
from encyclopaedia.models import Article
from django.template import Context, loader
from itertools import groupby
from collections import defaultdict

def article(request, article_id):
    article = Article.objects.get(pk=article_id)
    return HttpResponse(article.text)

def index(request):
    name_dict = {}
    name_list = groupby(sorted(list(Article.objects.all())),
                        key=lambda a: a.name[0])
    for k, v in name_list:
        name_dict[k] = list(v)

    template = loader.get_template('encyclopaedia/index.html')
    context = Context({
        'sections': sorted(name_dict.items()),
    })
    return HttpResponse(template.render(context))

def section(request, letter):
    q1 = Article.objects.filter(name__startswith=letter)

    template = loader.get_template('encyclopaedia/section.html')
    context = Context({
        'articles': [a for a in q1],
    })
    return HttpResponse(template.render(context))
