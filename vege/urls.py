from django.urls import path
from . import views

app_name = 'vege'

urlpatterns = [
    path('', views.recepies, name='recepies'),
    path('second/<int:blog_id>/', views.second, name='second'),
]
