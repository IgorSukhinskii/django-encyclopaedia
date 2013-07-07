from django.http import HttpResponse
from encyclopaedia.models import Article

def article(request, article_id):
	article = Article.objects.get(pk=article_id)
	return HttpResponse(article.text)
