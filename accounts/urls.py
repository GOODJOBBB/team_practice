from django.urls import path
from .views import co_signup
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('co_signup/',co_signup,name="co_signup"),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
]

