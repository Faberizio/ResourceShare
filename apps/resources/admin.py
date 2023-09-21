from django.contrib import admin
from apps.resources import models

# Register your models here.

class CustomRating(admin.ModelAdmin):
    list_display = (
        "user_id",
        "resources_id",
        "rate")
    
    def rating(self):
        return object.rate
    
class CustomReview(admin.ModelAdmin):
    list_display = (
        "username",
        "title",
        "get_body"
        )
    
    @admin.display(description="Body")    
    def get_body(self, obj):
        if len(obj.body) >50:
            return f"{obj.body[:50]}..."
        return obj.body
    
class CustomResources(admin.ModelAdmin):
    list_display = ("username",
                    "title",
                    "link",
                    "description",
                    "get_all_tags",
)
    @admin.display(description="Tags")
    def get_all_tags(self, obj):
        return obj.all_tags()
    
class CustomResourcesTag(admin.ModelAdmin):
    list_display = (
        'title',
        'tag'
    )    
    def title(self, obj):
        return obj.resources.title
    
admin.site.register(models.Tag)
admin.site.register(models.Category)
admin.site.register(models.Resources, CustomResources)
admin.site.register(models.ResourceTag, CustomResourcesTag)
admin.site.register(models.Review, CustomReview)
admin.site.register(models.Rating, CustomRating)


