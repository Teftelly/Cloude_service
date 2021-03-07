from django.urls import path

from . import views

urlpatterns = [
    # главная страница
    path('', views.index, name='index'),
    # страница с загрузкой и мгновенным отображением пользовательской картинки
    path('history_files/', views.user_history)
]