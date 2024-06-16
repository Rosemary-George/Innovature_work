# from django.shortcuts import render,redirect
# from django.http import JsonResponse
# from rest_framework import generics
# from .models import Product
# from .serializers import ProductSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# # class ProductListCreate(generics.ListCreateAPIView):
# #     queryset = Product.objects.all()
# #     serializer_class = ProductSerializer

# # class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = Product.objects.all()
# #     serializer_class = ProductSerializer

# # def Productdetails(request):
# #     obj = Product.objects.all()
# #     return render(request,"pview.html",{"data":obj})
# # def Productedit(request):
# #     userid = request.GET.get('uid')
# #     obb = Product.objects.filter(id=userid)
# #     return render(request,"productview.html",{"prod":obb})
# # def Productupdate(request):
# #     if request.method=='POST':
# #         nm = request.POST.get('name')
# #         idno = request.POST.get('uid')
# #         desc = request.POST.get('desc')
# #         price = request.POST.get('ps')
# #         Product.objects.filter(id=idno).update(name=nm,description=desc,price=price)
# #         return redirect("/fileApi/ProductDetails")
# #     return render(request,"productview.html")
# # def delete(request):
# #     userid = request.GET.get('uid')
# #     obb = Product.objects.filter(id=userid)
# #     obb.delete()
# #     return redirect("/products/ProductDetails")

# class ProductListCreate(APIView):
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from django.http import Http404
from django.urls import reverse
from django.shortcuts import redirect

class ProductListCreate(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SomeOtherView(APIView):
    def some_method(self, request):
        # Get a product instance
        product = Product.objects.get(pk=1)
        
        # Reverse URL with the pk argument
        url = reverse('product-detail', kwargs={'pk': product.pk})
        
        # Redirect to the product detail page
        return redirect(url)
class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
