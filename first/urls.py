from django.urls import path
from . import views

app_name = 'first'

urlpatterns = [
    path('', views.recepies, name='recepies'),
]
