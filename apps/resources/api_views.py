from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import DestroyAPIView,ListAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from .models import Resources, Category
from rest_framework.response import Response
from .serializers import ResourceSerializer, CategorySerializer, TagSerializer, CategoryModelSerializer, TagModelSerializer, ResourceModelSerializer
from . import serializers
from . import mixins


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def list_resources(request):
    queryset = (
        Resources.objects.select_related("user_id", "cat_id")
        .prefetch_related("tags")
        .all()
    )
    
    # Use the serializer to create the response
    response = ResourceSerializer(queryset, many=True).data
    return Response(response)

@api_view(['GET'])
def list_categories(request):
    queryset = Category.objects.all()
    response = CategoryModelSerializer(queryset, many=True).data
    return Response(response)


class FilterOutAdminResourcesMixin:
    def get_queryset(self):
        quesryset = Resources.objects.all()
        queryset = queryset.exclude(user_id__is_superuser__exact=True)
        return queryset
class ListResources(ListAPIView):
    authentication_classes = (BasicAuthentication, )
    permission_classes = (IsAuthenticated, )
    queryset = (
        Resources.objects.select_related("user_id", "cat_id")
        .prefetch_related("tags")
        .all()
    )
    serializer_class = ResourceModelSerializer
    
    

class DetailResource(RetrieveAPIView):
    lookup_field = "id" 
    queryset = (
        Resources.objects.select_related("user_id", "cat_id")
        .prefetch_related("tags")
        .all()
    )
    serializer_class = ResourceModelSerializer

# ViewSets can permit to perform CRUD
class ResourceViewSets(viewsets.ModelViewSet):
    queryset = (
        Resources.objects.select_related("user_id", "cat_id")
        .prefetch_related("tags")
        .all()
    )
    serializer_class = ResourceModelSerializer
    
class ResourceViewSetsFilterOutAdminResources(FilterOutAdminResourcesMixin,viewsets.ModelViewSet):
    queryset = (
        Resources.objects.select_related("user_id", "cat_id")
        .prefetch_related("tags")
        .all()
    )
    serializer_class = ResourceModelSerializer
    
class CategoryViewSets(mixins.DenyDeletionOfDefaultCategoryMixin, viewsets.ModelViewSet):
    queryset = (
        Category.objects.all()
    )
    serializer_class = CategoryModelSerializer
                                        

class DeleteCategory(mixins.DenyDeletionOfDefaultCategoryMixin, DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryModelSerializer
    

        