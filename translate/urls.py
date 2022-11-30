from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('processing/<int:pk>/', views.processing, name='processing'),
    path('file_status/<str:fileName>/', views.get_file_status, name='file_status'),
    path('edit/<str:fileName>/', views.edit_generated, name='edit_translated')
]
