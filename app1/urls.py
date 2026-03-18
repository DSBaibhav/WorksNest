from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('toggle/<int:id>/',views.toggle),
    path('delete/<int:id>/', views.delete),
    path('edit/<int:id>/',views.edit),
    path('clear/',views.clear_all),
]