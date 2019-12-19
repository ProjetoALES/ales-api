from django.urls import path, include

from rest_framework import routers

from .views import ProfessorViewSet

router = routers.SimpleRouter()
router.register(r'professors', ProfessorViewSet, basename='professors')

urlpatterns = router.urls
