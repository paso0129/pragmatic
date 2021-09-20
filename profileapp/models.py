from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    # 1 : 1매칭 프로파일의 주인이 누구인가
    # 연결해줌 원투원 (User와..) 온딜리트는 연결되어 있는 유저객체가
    # 없어질때 그와 연결된 프로필도 삭제
    # 캐스케이드 이 프로필도 없어지게 설정
    # related_user 는 따로 프로필에 바로 연결할수 있게 이름을 정해줌
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # upload to 저장될 경로 (root setting)미디어 밑에 프로파일이란 경로에 이미지 저장
    image = models.ImageField(upload_to='profiles/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    # 대화명
    message =  models.CharField(max_length=200, null=True)