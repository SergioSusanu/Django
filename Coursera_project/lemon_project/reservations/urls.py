from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('create',views.show_form),
    path('process',views.process_form),
]