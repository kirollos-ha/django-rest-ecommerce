from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET', 'POST'])
def api_root(request, format=None):
    return Response({'please select' : 'something'})

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_info = openapi.Info(
      title="Ecommerce Tipo",
      default_version='v1',
      description="Test description",
      terms_of_service="https://ricette.giallozafferano.it/Lasagne-alla-Bolognese.html",
      contact=openapi.Contact(email="particular.kenobi@protonmail.com"),
      license=openapi.License(name="WTF Public License"),
   )
schema_view = get_schema_view(
    schema_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', api_root, name='at_the_center_of_it_all'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair_view'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_refresh_view'),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    

    path('authentication/', include('authentication.urls')),
    path('shop/', include('shop.urls')),
    path('admin/', admin.site.urls),
]
