from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs,name='blog_list'),
    path('detail/<int:blog_id>', views.detail ,name='blog_detail'),
]