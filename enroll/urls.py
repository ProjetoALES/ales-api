from django.urls import path, include

from rest_framework import routers

from .views import ProfessorViewSet, StudentViewSet

router = routers.SimpleRouter()
router.register(r'professors', ProfessorViewSet, basename='professors')
router.register(r'students', StudentViewSet, basename='students')

urlpatterns = router.urls
