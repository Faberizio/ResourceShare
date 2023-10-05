from django.urls import path
from rest_framework import routers
from . import views
from . import api_views

router = routers.SimpleRouter()
router.register("api/v3/resource/", api_views.ResourceViewSets)
router.register("api/v3/category/", api_views.CategoryViewSets)

api_urlpatterns = [
    path("api/v1/resource", api_views.list_resources, name="list_resources"),
    path("api/v1/categories", api_views.list_category, name="list_categories"),
    path("api/v2/resource/", api_views.ListResource.as_view(), name="list-resources-class"),
    path("api/v2/resource/<int:id>", api_views.ListResource.as_view(), name="detail-resource-class"),
    path(
        "api/v2/category/<int:pk>/",
        api_views.DeleteCategory.as_view(),
        name="delete-category-class",
    ),
]

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('resource/<int:id>/', views.resource_detail, name='resource-detail'),
    path('resource/post/', views.resource_post, name="resource-post"),
    *api_urlpatterns,
    *router.urls,
]
