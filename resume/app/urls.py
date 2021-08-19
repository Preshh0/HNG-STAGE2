from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.contact_view, name='index')
]