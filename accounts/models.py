from django.db import models
from django.contrib.auth.models import User




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ID = models.CharField(max_length=200)
    기업명 = models.CharField(max_length=200)
    주소 =  models.CharField(max_length=200)
    홈페이지주소 =  models.CharField(max_length=200)
    대표자명 = models.CharField(max_length=200)
    전화번호 =  models.CharField(max_length=200)
    근로자수 = models.CharField(max_length=200)
    설립일 =  models.CharField(max_length=200)
    업종 =  models.CharField(max_length=200)

    ID = models.CharField(max_length=200)
    이름 = models.CharField(max_length=200)
    생년월일 =models.CharField(max_length=200)
    주소 = models.CharField(max_length=200)
    휴대폰번호 =models.CharField(max_length=200)
    최종학력 = models.CharField(max_length=200)
    자격증 = models.CharField(max_length=200) 
    경력있는분야 = models.CharField(max_length=200)
    관심있는분야 = models.CharField(max_length=200)
    희망연봉 = models.CharField(max_length=200)
    미니자기소개서 = models.TextField(max_length=500)