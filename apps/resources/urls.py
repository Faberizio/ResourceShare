from django.urls import path
from . import views
from . import api_views

api_urlpatterns = [
    path("api/v1/resource", api_views.list_resources, name="list_resources"),
]
urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('resource/<int:id>/', views.resource_detail, name='resource-detail'),
    path('resource/post/', views.resource_post, name="resource-post"),
    *api_urlpatterns,
]
