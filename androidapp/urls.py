from rest_framework import routers
from django.urls import path, include
from .views import TitleViewSet, DescViewSet 

router = routers.DefaultRouter()
router.register(r'TitleViewSet', TitleViewSet)
router.register(r'DescViewSet', DescViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
