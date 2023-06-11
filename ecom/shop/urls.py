from django.urls import path
from shop import views
from rest_framework.urlpatterns import format_suffix_patterns


# path('users/<int:user_id>/', include('shop.urls'))
urlpatterns = format_suffix_patterns([
    path('', views.hello_please_work, name='hello'),
    path('users/<int:user_id>/cart/', views.user_cart, name='cart'),
    path('users/<int:user_id>/cart/<int:product_id>/', views.pass_ma_figo, name='passcart'),
    path('users/<int:user_id>/products/', views.user_products, name='products'),
    path('users/<int:user_id>/products/<int:product_id>', views.pass_ma_figo, name='passpro'),
])
