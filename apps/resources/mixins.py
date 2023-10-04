from rest_framework.exceptions import PermissionDenied

DEFAULT_CATEGORY_ID = 1

class DenyDeletionOfDefaultCategoryMixin:
    # Wewant to  get the category ID we are about to delete
    # We want to compare it with the DEFAULT_CATEGORY_ID
    # If True, raise an exception

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "destroy":
            pk = self.kwargs["pk"]
            deleted_queryset = queryset.get(pk=pk)
            if deleted_queryset.pk == DEFAULT_CATEGORY_ID:
                raise PermissionDenied(
                    f"Not allowed to delete category with id {pk}"
                )
        return queryset # always returns queryset