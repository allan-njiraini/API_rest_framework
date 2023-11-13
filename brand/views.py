from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from brand.models import Product
from brand.serializers import ProductSerializer


@api_view(['GET'])
def product_list(request):
    """
    List all products.
    """

    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
