from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['ID', '이름', '생년월일','자격증','휴대폰번호', '최종학력', '경력있는분야', '관심있는분야', '희망연봉', '미니자기소개서','기업명', '주소', '홈페이지주소', '대표자명', '전화번호', '근로자수', '설립일','업종',]
         
 


        