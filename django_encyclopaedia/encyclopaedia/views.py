from django.http import HttpResponse
from encyclopaedia.models import Article
from django.template import Context, loader

def article(request, article_id):
	article = Article.objects.get(pk=article_id)
	return HttpResponse(article.text)

def index(request):
	letter_list = Article.objects.all()
	x=[a.name[0] for a in letter_list]
	letter_list=sorted(list(set(x)))

	template = loader.get_template('encyclopaedia/index.html')
	context = Context({
        'sections': letter_list,
    })
	return HttpResponse(template.render(context))

def section(request, letter):
	q1 = Article.objects.filter(name__startswith=letter)

	template = loader.get_template('encyclopaedia/section.html')
	context = Context({
        'articles': [a for a in q1],
    })
	return HttpResponse(template.render(context))
