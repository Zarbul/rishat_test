from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from src.api import views

urlpatterns = [
    path('buy/<int:pk>', views.ItemBuy.as_view(), name='buy_page'),
    path('item/<int:pk>', views.ItemView.as_view(), name='item'),
    path('item/', views.ItemList.as_view(), name='item_list'),
    path('', TemplateView.as_view(template_name='main.html'), name='main_page'),
]

