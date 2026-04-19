from django.urls import path
from . import views

urlpatterns = [
    path('photo/<int:photo_id>/', views.photo, name='photo'),
]