from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('django.contrib.auth.urls')),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

handler404 = views.error_404_view