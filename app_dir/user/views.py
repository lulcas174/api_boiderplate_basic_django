from app_dir.user.models import Users
from app_dir.user.serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet


class UserView(ModelViewSet):
    queryset= Users.objects.all()
    serializer_class = UserSerializer
