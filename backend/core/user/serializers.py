from core.abstract.serializers import AbstractSerializer

from core.user.models import User


class UserSerializer(AbstractSerializer):
    # Rewriting some fields like the public id to be represented as the id of the object

    class Meta:
        model = User
        # List of all the fields that can be included in a request or a response
        fields = ['id', 'username', 'first_name', 'last_name', 'bio', 'avatar', 'email', 'is_active',
                  'created', 'updated']
        # List of all the fields that can only be read by the user
        read_only_field = ['is_active']