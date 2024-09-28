from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('upload/', views.upload_file, name='upload_file'),
    path('result/<int:sql_file_id>/', views.result, name='result'),
]

