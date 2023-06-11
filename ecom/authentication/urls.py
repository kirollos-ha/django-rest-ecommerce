from django.urls import path, include
import authentication.views as views
from rest_framework.urlpatterns import format_suffix_patterns

shop_user_list = views.ShopUserViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})
shop_user_detail = views.ShopUserViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('', views.api_root, name='root'),
    path('users/', shop_user_list, name='shopuser-list'),
    path('users/<int:pk>/', shop_user_detail, name='shopuser-detail'), 
])
#il name=... ha un ruolo fondamentale nella ricerca dell'url che non ho ancora effettivamente capito

urlpatterns += [
    path('something-auth/', include('rest_framework.urls')),
]
