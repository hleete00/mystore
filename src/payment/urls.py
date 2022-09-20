from django.urls import path, include
from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.CartView, name='cart'),
    path('orderplaced/', views.order_placed, name='order-placed'),
    # path('error/', views.Error.as_view(), name='error'),
    path('webhook/', views.stripe_webhook),
]
