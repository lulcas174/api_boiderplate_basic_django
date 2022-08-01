from app_dir.user.views import UserView
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', UserView)
urlpatterns = [
    path('', include(router.urls))
]
