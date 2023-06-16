from shop.models import Order, Product
from shop.serializers import OrderSerializer, ProductSerializer
from authentication.models import ShopUser

def get_user_cart(user_id):
    return ShopUser.objects.get(id=user_id).orders_made.all()

def get_user_products(user_id):
    return ShopUser.objects.get(id=user_id).products.all()

def save_or_bad_request(request_data):
   serializer = OrderSerializer(data=request_data)
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(status = status.HTTP_400_BAD_REQUEST)


from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def hello_please_work(request, user_id, format=None):
    return Response({'hello' : 'world'})

@api_view(['GET', 'POST'])
def user_cart(request, user_id, format=None):
    # login required
    if request.user.id != user_id:
        return Response(status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        serializer = OrderSerializer(get_user_cart(user_id), many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        return save_or_bad_request(request.data)

@api_view(['GET', 'POST'])
def user_products(request, user_id, format=None):
    if request.method == 'GET':
        serializer = OrderSerializer(get_user_products(user_id), many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        if request.user.id != user_id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return save_or_bad_request(request.data)
    
@api_view(['GET', 'POST'])
def pass_ma_figo(request, user_id, product_id):
    return Response({'status' : status.HTTP_404_NOT_FOUND})

from rest_framework.permissions import IsAuthenticated
from rest_flex_fields import FlexFieldsModelViewSet 
from authentication.serializers import ShopUserSerializer
from authentication.models import ShopUser
# lo usa il tutorial e mi spaventa non farlo
# non ho idea di cosa sia, e a questo punto non credo di volerlo sapere

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ma_vaffanculo(request, format=None):
    return Response({ 'mannaggia' : 'la mignotta' })
