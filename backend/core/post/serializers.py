from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.abstract.serializers import AbstractSerializer
from core.post.models import Post
from core.user.models import User
from core.user.serializers import UserSerializer

class PostSerializer(AbstractSerializer):

    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')
    liked = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    def validate_author(self, value):
        print(f"request serialzier in validate author: {self.context["request"]}\n")
        if self.context["request"].user != value:
            raise ValidationError("You can't create a post for another user.")
        return value
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep["author"])
        rep["author"] = UserSerializer(author).data
        return rep
    
    def get_liked(self, instance):
        
        request = self.context.get('request', None)
        # print(f"Request trong get_liked: {request.__dict__}")
        if request is None or request.user.is_anonymous:
            return False

        return request.user.has_liked(instance)

    def get_likes_count(self, instance):
        # print(f"Instance trong get_likes_count: {instance.__dict__}")
        return instance.liked_by.count()

    class Meta:
        model = Post
        # List of all the fields that can be included in a request or a response
        fields = ['id', 'author', 'body', 'likes_count', 'liked', 'edited', 'created', 'updated']
        read_only_fields = ["edited"]