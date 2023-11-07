from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('create-post/', views.create_post, name='post'),
    path('edit-post/<int:pk>', views.edit_post, name='edit_post'),
    path('home/<str:ordering>', views.post_ordering, name='post_ordering')
]