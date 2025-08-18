from django.urls import path
from .views import menu_items_view

urlpatterns = [
    path('menu/', menu_items_view, name='menu_items'),
    
]