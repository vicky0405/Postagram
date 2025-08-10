from core.abstract.serializers import AbstractSerializer

from core.user.models import User

from django.conf import settings

class UserSerializer(AbstractSerializer):
    # Rewriting some fields like the public id to be represented as the id of the object
    def to_representation(self, instance):
        print("self.context in userserializer: ", self.context)
        representation = super().to_representation(instance)
        if not representation['avatar']:
            representation['avatar'] = settings.DEFAULT_AVATAR_URL
            return representation
        if settings.DEBUG:  # Debug enabled for dev
            request = self.context['request']
            representation['avatar'] = request.build_absolute_uri(representation['avatar'])
        return representation
    
    class Meta:
        model = User
        # List of all the fields that can be included in a request or a response
        fields = ['id', 'username', 'first_name', 'last_name', 'bio', 'avatar', 'email', 'is_active',
                  'created', 'updated']
        # List of all the fields that can only be read by the user
        read_only_field = ['is_active']