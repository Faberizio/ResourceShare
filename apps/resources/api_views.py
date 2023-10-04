from rest_framework.decorators import api_view
from .models import Resources
from rest_framework.response import Response

@api_view(['GET'])
def list_resources(request):
    queryset = (
        Resources.objects.select_related("user_id", "cat_id")
        .prefetch_related("tags")
        .all()
    )
    
    response = [
        {
            "title": resource.title,
            "link": resource.link,
            "user": {
                "id": resource.user_id.id,
                "username": resource.user_id.username,
            },
            "category": resource.cat_id.cat,
            "tags": [tag.name for tag in resource.tags.all()],
        }
        for resource in queryset
    ]

    return Response(response)
