from django.urls import path
from.import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('products', views.products, name = 'products'),
    path('contact_us', views.contact_us, name = 'contact_us'),
    path('product1', views.product1, name = 'product1'),
    path('product2', views.product2, name = 'product2'),
    path('product3', views.product3, name = 'product3'),
    path('order_now', views.order_now, name = 'order_now'),
    path('order_success', views.order_success, name = 'order_success'),
]