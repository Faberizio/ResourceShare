from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("user_list/", views.user_list, name="user_list"),
    path('login/', views.login_view, name="login-view"),
    path("profile/", views.profile, name="profile"),
    path('logout/', LogoutView.as_view(), name='logout'),
]

