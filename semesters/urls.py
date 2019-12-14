from django.urls import path, include

from rest_framework import routers

from .views import SemesterViewSet

router = routers.SimpleRouter()
router.register(r'', SemesterViewSet, basename='semesters')

urlpatterns = router.urls
