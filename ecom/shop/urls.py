from django.urls import path, include
from shop import views
from rest_framework.urlpatterns import format_suffix_patterns

# path('users/<int:user_id>/', include('shop.urls'))
urlpatterns = format_suffix_patterns([
    path('', views.hello_please_work, name='hello'),
    path('cart/', views.user_cart, name='cart'),
    path('cart/<int:product_id>/', views.pass_ma_figo, name='passcart'),
    path('products/', views.user_products, name='products'),
    path('products/<int:product_id>/', views.pass_ma_figo, name='passpro'),
    path('kitemmuort', views.ma_vaffanculo, name='vaffanculo'),
])
