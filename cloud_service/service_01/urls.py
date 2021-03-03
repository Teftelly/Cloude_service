from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('history_files/', views.user_history)
]