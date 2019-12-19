from django.contrib import admin
from django.urls import path, include
from login.views import AuthenticatedView

base_api_path = 'api/v1'

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),

    # auth
    path('{}/token/'.format(base_api_path), include('login.urls')),
    path('{}/auth/'.format(base_api_path), include('djoser.urls')),
    path('{}/auth/'.format(base_api_path), include('djoser.urls.jwt')),
    path('{}/ping/'.format(base_api_path),
         AuthenticatedView.as_view(), name='test_auth_view'),

    # semesters
    path('{}/semesters/'.format(base_api_path), include('semesters.urls')),

    # professors
    path('{}/users/'.format(base_api_path), include('enroll.urls'))
]
