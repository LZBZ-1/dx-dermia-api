# melanoma_service/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('analyze', views.analyze_melanoma, name='analyze_melanoma'),
]