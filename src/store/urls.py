from django.urls import path
from . import views


app_name = 'store'

urlpatterns = [
    path('', views.product_all, name='product-all'),
    path('item/<slug:slug>/', views.product_detail, name='product-detail'),
    path('shop/<slug:category_slug>/',
         views.category_list, name='category-list'),
]
