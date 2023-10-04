from . import serializers

class RestrictInactiveUserMixin:
    def get_serializer_class(self):
        if not self.user.is_active:
            return serializers.UserUpdateModelSerializer
        else:
            return serializers.UserModelSerializer
        