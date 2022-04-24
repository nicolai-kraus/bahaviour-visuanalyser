from django.urls import path
from . import views

urlpatterns = [
        path('', views.entry, name='entry'),
        path('success/', views.success, name='success'),
        path('entry/', views.entry, name='entry'),
        ]
