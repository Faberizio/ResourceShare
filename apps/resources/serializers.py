from rest_framework import serializers
from .models import Category, Resources, Tag

class TagSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    created_at = serializers.DateTimeField()
    modified_at = serializers.DateTimeField()

class ResourceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    link = serializers.URLField()
    cat = serializers.CharField()
    tags = TagSerializer(many=True)

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    cat_id = serializers.CharField()
    created_at = serializers.DateTimeField()
    modified_at = serializers.DateTimeField()



class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"  # Corrected the model name

class ResourceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = (
            "id",
            "title",
            "description",
            "link",
            "user_id",
            "cat_id",
            "tags"
        )
