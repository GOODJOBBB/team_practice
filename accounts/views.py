from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login 
from .forms import ProfileForm
from django.contrib.auth.models import User

# Create your views here.

def co_signup(request):
    context=dict()
    context['profileForm'] = ProfileForm()
    context['userForm'] = UserCreationForm()

    if request.method == "POST":
        save_user = UserCreationForm(request.POST)
        
        save_profile = ProfileForm(request.POST)
        if save_user.is_valid() and save_profile.is_valid():
            save_user.save()
            tmp_profile = save_profile.save(commit=False)
            tmp_profile.user = save_user.id 
            
            # tmp_profile.user = User.objects.get(id = save_user.id )
            #User.objects.all.order_by("-id").last()
        
            tmp_profile.save()
    if request.method == "POST":
        form = ProfileForm()

        if form.is_valid():
            form.save()
            

            user = User.objects.create_user(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"])

            ID = form.cleaned_data["ID"]
            profile = Profile(user=user, ID=ID)
            profile.save()



            기업명 = form.cleaned_data["기업명"]
            profile = Profile(user=user, 기업명=기업명)
            profile.save()



            주소 = form.cleaned_data["주소"]
            profile = Profile(user=user, 주소=주소)
            profile.save()

            홈페이지주소 = form.cleaned_data["홈페이지주소"]
            profile = Profile(user=user, 홈페이지주소=홈페이지주소)
            profile.save()

            대표자명 = form.cleaned_data["대표자명"]
            profile = Profile(user=user, 대표자명=대표자명)
            profile.save()

            전화번호 = form.cleaned_data["전화번호"]
            profile = Profile(user=user, 전화번호=전화번호)
            profile.save()

            근로자수 = form.cleaned_data["근로자수"]
            profile = Profile(user=user, 근로자수=근로자수)
            profile.save()

            설립일 = form.cleaned_data["설립일"]
            profile = Profile(user=user, 설립일=설립일)
            profile.save()

            업종 = form.cleaned_data["업종"]
            profile = Profile(user=user, 업종=업종)
            profile.save()







            auth.login(request, user)

            return render(request, 'co_mypage.html',context)

        else:
            context['userForm'] = save_form #사용자가 입력한 데이터와 실패한 이유가 담긴 form 
            return render(request, 'registration/co_signup.html',context)


    return render(request, 'registration/co_signup.html',context)



def user_signup(request):
    context=dict()
    context['profileForm'] = ProfileForm()
    context['userForm'] = UserCreationForm()

    if request.method == "POST":
        save_user = UserCreationForm(request.POST)
        save_profile = ProfileForm(request.POST)
        if save_user.is_valid() and save_profile.is_valid():
            save_user.save()
            tmp_profile = save_profile.save(commit=False)
            tmp_profile.user = save_user.id 
            
            # tmp_profile.user = User.objects.get(id = save_user.id )
            #User.objects.all.order_by("-id").last()
        
            tmp_profile.save()
    if request.method == "POST":
        form = ProfileForm()

        if form.is_valid():
            form.save()
            

            user = User.objects.create_user(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"])

            ID = form.cleaned_data["ID"]
            profile = Profile(user=user, ID=ID)
            profile.save()



            이름 = form.cleaned_data["이름"]
            profile = Profile(user=user, 이름=이름)
            profile.save()

            생년월일 = form.cleaned_data["생년월일"]
            profile = Profile(user=user, 생년월일=생년월일)
            profile.save()
 
            주소 = form.cleaned_data["주소"]
            profile = Profile(user=user, 주소=주소)
            profile.save()

            휴대폰번호 = form.cleaned_data["휴대폰번호"]
            profile = Profile(user=user, 휴대폰번호=휴대폰번호)
            profile.save()

            최종학력 = form.cleaned_data["최종학력"]
            profile = Profile(user=user, 최종학력=최종학력)
            profile.save()

            자격증 = form.cleaned_data["자격증"]
            profile = Profile(user=user, 자격증=자격증)
            profile.save()

            경력있는분야 = form.cleaned_data["경력있는분야"]
            profile = Profile(user=user, 경력있는분야=경력있는분야)
            profile.save()

            관심있는분야 = form.cleaned_data["관심있는분야"]
            profile = Profile(user=user, 관심있는분야=관심있는분야)
            profile.save()

            희망연봉 = form.cleaned_data["희망연봉"]
            profile = Profile(user=user, 희망연봉=희망연봉)
            profile.save()

            미니자기소개서 = form.cleaned_data["미니자기소개서"]
            profile = Profile(user=user, 미니자기소개서=미니자기소개서)
            profile.save()






            auth.login(request, user)

            return render(request, 'user_home.html',context)

        else:
            context['userForm'] = save_user and save_profile #사용자가 입력한 데이터와 실패한 이유가 담긴 form 
            return render(request, 'registration/user_signup.html',context)


    return render(request, 'registration/user_signup.html',context)
# @login_required
# def userinfo(request):
