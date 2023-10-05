from rest_framework import serializers
from .. import models


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"  # special string to serialize all model's attribute


class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = "__all__"


class ResourceModelSerializer(serializers.ModelSerializer):
    cat_id = CategoryModelSerializer()
    tags = TagModelSerializer(many=True)

    class Meta:
        model = models.Resources
        # two options
        # Specify the fields we want our serializer to serialize
        # Omit fields that our serializer shouldn't serialize
        fields = (
            "id",
            "title",
            "description",
            "link",
            "cat_id",
            "tags",
        )