from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


# pk확인해서 그 유저 오브젝트가 실제로 보는 request 유저와 동일한지 확인을 하고
# 아니면 forbidden 출력
from articleapp.models import Article


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        if not article.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated
