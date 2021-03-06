from django.contrib.auth.models import User
from django.db import models

# Create your models here.auto_now_Add
from projectapp.models import Project


class Article(models.Model):
    #회원 탈퇴 했을때 게시글이 사라지지 않고 주인없음 느낌
    # related name 접근시 사용할 이름
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)


