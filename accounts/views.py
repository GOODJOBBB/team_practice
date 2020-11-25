from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm #유저생성 모델폼
from django.contrib.auth import authenticate, login 
# Create your views here.

def co_signup(request):
    context=dict()
    if request.method == "POST":
        save_form = UserCreationForm(request.POST)
        if save_form.is_valid():
            save_form.save()

            user = authenticate(username = save_form.cleaned_data['username'],
                                password = save_form.cleaned_data['password1'])

            login(request, user)

            return render(request, 'co_mypage.html',context)

        else:
            context['userForm'] = save_form #사용자가 입력한 데이터와 실패한 이유가 담긴 form 
            return render(request, 'registration/co_signup.html',context)

    context['userForm'] = UserCreationForm()

    return render(request, 'registration/co_signup.html',context)

# @login_required
# def userinfo(request):
