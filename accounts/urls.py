from django.urls import path
from .views import co_signup, user_signup
from django.contrib.auth.views import LoginView, LogoutView
# from django.conf import settings

urlpatterns = [
    path('co_signup/',co_signup,name="co_signup"),
    path('user_signup/',user_signup,name="user_signup"),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    # path('mypage/',userinfo,name='mypage'),
]

