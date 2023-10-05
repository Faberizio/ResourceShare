from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Resources, Category
from .serializers import serializers
from .serializers.serializers import ResourceModelSerializer

from . import mixins


@api_view(["GET"])
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def list_resources(request):
    queryset = (
        Resources.objects.select_related("user_id", "cat_id")
        .prefetch_related("tags")
        .all()
    )

    #  response = [
    #      {
    #          "title": query.title,
    #          "link": query.link,
    #          "user": {
    #              "id": query.user_id.id,
    #              "username": query.user_id.username,
    #          },
    #          "category": query.cat_id.cat,
    #          "tags": query.all_tags(),
    #      }
    #      for query in queryset
    #  ]
    response = serializers.ResourceModelSerializer(queryset, many=True)
    # transform to JSON before returning
    return Response(response.data)


@api_view(["GET"])
def list_category(request):
    queryset = Category.objects.all()

    #  response = [
    #      {
    #          "id": query.id,
    #          "name": query.cat,
    #      }
    #      for query in queryset
    #  ]
    # call the serialzier and pass in the queryset
    # set the attribute `many=True`
    # to indicate that we are expected many objects
    response = serializers.CategorySerializer(queryset, many=True)
    return Response(response.data)


class ListResource(ListAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = (
        Resources.objects.select_related("user_id", "cat_id")
        .prefetch_related("tags")
        .all()
    )
    serializer_class = serializers.ResourceModelSerializer


class DetailResource(RetrieveAPIView):
    lookup_field = "id"  # by default, the lookup field is `pk`
    queryset = (
        Resources.objects.select_related("user_id", "cat_id")
        .prefetch_related("tags")
        .all()
    )
    serializer_class = serializers.ResourceModelSerializer


# ViewSets can permit us to perform the CRUD operations in one class based view.
class ResourceViewSets(viewsets.ModelViewSet):  # <model>ViewSets
    queryset = (
        Resources.objects.select_related("user_id", "cat_id")
        .prefetch_related("tags")
        .all()
    )
    serializer_class = serializers.ResourceModelSerializer


class CategoryViewSets(
    mixins.DenyDeletionOfDefaultCategoryMixin, viewsets.ModelViewSet
):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryModelSerializer


class DeleteCategory(mixins.DenyDeletionOfDefaultCategoryMixin, DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryModelSerializer