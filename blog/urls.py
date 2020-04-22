from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog),
    path('<int:blog_id>/', views.text1),
]