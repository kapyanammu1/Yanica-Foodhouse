from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.item_list, name='item_list'),
    path('items/create/', views.item_create, name='item_create'),
    path('items/<int:pk>/edit/', views.item_edit, name='item_edit'),
    path('items/<int:pk>/delete/', views.item_delete, name='item_delete'),
    path('send_email/', views.sendEmail, name='send_email'),
]