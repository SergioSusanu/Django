from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('', views.home, name='index'),
    path('create/',views.show_form, name='show_form'),
    path('process',views.process_form, name='process_form'),
    path('categories', views.show_menu_categories, name='categories'),
    path('login/', views.login, name='login'),
]