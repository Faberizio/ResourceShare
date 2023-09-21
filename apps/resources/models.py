from django.db import models
from django.contrib.postgres.fields import ArrayField
from apps.resources import validators
from django.db.models import UniqueConstraint

from apps.core.models import CreatedModifiedDateTime


# Create your models here.
class Tag(CreatedModifiedDateTime):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(CreatedModifiedDateTime):
    cat = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.cat
    
class Resources(CreatedModifiedDateTime):
    user_id = models.ForeignKey("user.User", on_delete=models.SET_NULL, null=True)
    cat_id = models.ForeignKey("resources.Category", default=1, on_delete=models.SET_DEFAULT)
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=500)
    tags = models.ManyToManyField("resources.Tag", through="ResourceTag")
    #rating = models.ManyToManyField("resources.Tag", through="ResourceRating")
    #tags = models.ManyToManyField("resources.Tag", through="ResourceTag")= ArrayField(base_field=models.IntegerField()) # INT ARRAY
    
    class Meta:
        verbose_name_plural = "Resources"

    def __str__(self):
        return f"{self.user_id.username} - {self.title}"

    @property
    def username(self):
        return self.user_id.username
    
    def user_title(self):
        return self.title # check if is user_id.title
    
    def all_tags(self):
        return ", ".join([tag.name for tag in self.tags.all()])

class ResourceTag(CreatedModifiedDateTime):
    modified_at = None
    resources = models.ForeignKey("resources.Resources", on_delete=models.CASCADE)
    tag = models.ForeignKey("resources.Tag", on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["resources", "tag"],
                name="resource_tag_unique",
                condition=models.Q(tag__isnull=False),
            )
        ]
        
        
    def title(self):
        return self.resources.title
    
    def tag_name(self):
        return self.tag.name
        
class Review(CreatedModifiedDateTime):
    user_id = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL)
    resources_id = models.ForeignKey("resources.Resources", on_delete=models.CASCADE)
    body = models.TextField()
     # ForeignKey to link each review to a resource
    resource = models.ForeignKey(Resources, related_name='reviews', on_delete=models.CASCADE)
    
    # Field to store the rating for the review
    rating = models.PositiveIntegerField(default=0)  # You can adjust the field type as needed


    
    def __str__(self):
        return f"{self.user_id.username} ({self.resources_id.title}"
    
    def username(self):
        return self.user_id.username
    
    def title(self):
        return self.resources_id.title
    
    
    
    
class Rating(CreatedModifiedDateTime):
    user_id = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL)
    resources_id = models.ForeignKey("resources.Resources", on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[validators.check_rating_range]) # CHCK(rate > 0 and rate < 5)
    
    @property
    def username(self):
        return self.user_id.username
    
    def __str__(self):
        return f"{self.user_id.username}: {self.rate}"
    
    
    