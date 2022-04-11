from django.urls import path

from base import views

urlpatterns = [
    path('', views.home, name="index"),
    path('generator/<int:fid>', views.generate_table, name="generator")
]
