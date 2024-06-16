from django.urls import path
from .views import create_event, index

urlpatterns = [
    path('', index, name='index'),
    path('create_event/', create_event, name='create_event'),
]