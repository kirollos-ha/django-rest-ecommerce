from rest_framework import viewsets

from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ShopUser

from .serializers import ShopUserSerializer

@api_view()
def api_root(request):
    return Response({"some" : "body once told me"})

class ShopUserViewSet(viewsets.ModelViewSet):
    """
    get post et al per user
    """
    queryset = ShopUser.objects.all()
    serializer_class = ShopUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
