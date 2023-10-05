from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from apps.user import api_views  # Import api_views here

api_urlpatterns = [
    path('api/v1/login', api_views.UserLogin.as_view(), name='user-login-class'),
    path("api/v1/profile/", api_views.UserProfile.as_view(), name="user-profile-class"),
]

urlpatterns = [
    path("user_list/", views.user_list, name="user_list"),
    path('login/', views.login_view, name="login-view"),
    path("profile/", views.profile, name="profile"),
    path("update/<int:id>/", views.UpdateUser.as_view(), name="update-user"),
    path('logout/', LogoutView.as_view(), name='logout'),
    *api_urlpatterns,
]
