

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import EventViewSet



router = DefaultRouter()

router.register('events', EventViewSet)

urlpatterns = [
   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('',include(router.urls)),
]

urlpatterns += router.urls