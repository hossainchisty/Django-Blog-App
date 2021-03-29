from django.urls import path
from . views import *
from . import views


urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('post_detail/<int:pk>' ,PostView.as_view(), name="post_detail"),
    path('post_create/',CreatePostView.as_view(), name="create_post"),
    path('post_update/<pk>', POSTUpdateView.as_view(), name="post_edit"),
    path('post_delete/<pk>', POSTDeleteView.as_view(), name="post_delete"),
    path('result/', views.search, name="result")
    
]