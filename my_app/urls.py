from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('service/', views.service, name='service'),
    path('products/', views.ProductsView.as_view(), name='products'),
    path('products/<str:id>/', views.product_detail, name= 'product-detail'),
    # path('products/<str:id>/', views.product_detail, name= 'product-detail'),

]