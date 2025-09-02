from django.urls import path
from MainApp import views
from MainApp.views import items_list, item_detail



urlpatterns = [
    path('', views.home, name='main_page'),
    path('about/', views.about, name='about'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('items/', views.items_list, name='items_list'),
    path('items/', items_list, name='items_list'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),
    ]