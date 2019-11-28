from django.contrib import admin
from django.urls import path, include
from login.views import AuthenticatedView

base_api_path = 'api/v1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('{}/token/'.format(base_api_path), include('login.urls')),
    path('{}/ping/'.format(base_api_path),
         AuthenticatedView.as_view(), name='test_auth_view')
]
