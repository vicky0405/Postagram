from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from core.user.serializers import UserSerializer
from core.user.models import User


class UserViewSet(viewsets.ModelViewSet):
    print("UserViewSet initialized")
    http_method_names = ('patch', 'get')
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)

    def get_object(self):
        print("get_object called")
        obj = User.objects.get_object_by_public_id(self.kwargs['pk'])

        self.check_object_permissions(self.request, obj)

        return obj

    