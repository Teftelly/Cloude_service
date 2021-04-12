from django.urls import path

from . import views

urlpatterns = [
    # главная страница
    path('main_page/', views.Poop_home),
    # Страница авторизации
    path('authorization/', views.Poop_authorization),
    # Страница регистрации
    path('registration/', views.Poop_registration),
    # Страница хранилища
    path('personal_page/', views.Poop_storage),
    # страница с загрузкой и мгновенным отображением пользовательской картинки
    path('generate_new/', views.user_history),
    # Страница просмотра старой записи <int:service_01_user_history_id>
    path('history/<int:user_history_id>/', views.History)
]