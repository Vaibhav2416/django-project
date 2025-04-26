from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
# Create your views here.
# ["GET","POST"]
@api_view() #api_view will convert your simple view function # into django-rest-framework view # Provides methods like [GET,POST,PUT,DELETE,PATCH]
def get_products_view(request):
    products=Product.objects.all() 
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data,status=200) #JSON Object
    

@api_view() #By_default method - GET
def get_single_product(request,id):
    return Response(f"Single Product {id}")
    

    
    
    


    

