from django.forms.models import model_to_dict
from products.models import Product
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer
# Create your views here.


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({'invalid': 'not good data'}, status=400)


# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all()
#     data = {}

#     if instance:
#         # instance = serializer.save()
#         data = ProductSerializer(instance).data
#     return Response(data)
