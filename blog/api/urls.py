from django.urls import path
from . import views


urlpatterns = [
    path('', views.ApiOverview, name='ApiOverview'),
    path('post-list/', views.postList, name='PostList'),
    path('post-detail/<int:pk>', views.postDetail, name='PostDetail'),
    path('post-create/', views.postCreate, name='PostCreate'),
    path('post-update/<int:pk>', views.postUpdate, name='PostUpdate'),
    path('post-delete/<int:pk>', views.postDelete, name='PostDelete'),
]