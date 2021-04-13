from django.urls import path

from . import views

urlpatterns = [
    # главная страница
    path('main_page/', views.Poop_home, name='home'),
    # Страница авторизации
    path('authorization/', views.Poop_authorization, name='author'),
    # Страница регистрации
    path('registration/', views.Poop_registration, name='registr'),
    # Страница хранилища
    path('personal_page/', views.Poop_storage, name='storage'),
    # страница с загрузкой и мгновенным отображением пользовательской картинки
    path('generate_new/', views.user_history, name='new'),
    # Страница просмотра старой записи <int:service_01_user_history_id>
    path('history/<int:user_history_id>/', views.History, name='history'),

    path('logout/', views.logout_view, name='logout'),
]