from . import views
from django.urls import path
app_name = 'vege'

urlpatterns = [
    path('', views.recepies, name= 'recepies'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
]