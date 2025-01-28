from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from gob.views.api_auth_rights import get_user_rights

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
    path('api-auth-rights/', get_user_rights, name='api_auth_rights'),
    path('admin/', admin.site.urls),
    path('gob/', include('gob.urls')),
]
