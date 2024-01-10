from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import serializers, status
from rest_framework.response import Response

from users.models import User

from .models import Category, Product
from .services import ProductCoordinatorService, ProductPhotoService, ProductKeywordService, ProductService


class ProductCreateApi(APIView):
    permission_classes=(AllowAny,)
    
    class ProductCreateInputSerializer(serializers.Serializer):
        name = serializers.CharField()
        category = serializers.CharField()
        keywords = serializers.ListField(required=False)
        basic_price = serializers.CharField()
        option = serializers.CharField()
        product_photos = serializers.ListField(required=False)
        info = serializers.CharField()
        notice = serializers.CharField()
        period = serializers.CharField()
        transaction_direct = serializers.BooleanField()
        transaction_package = serializers.BooleanField()
        refund = serializers.CharField()
    
    def post(self,request):
        serializers = self.ProductCreateInputSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        data = serializers.validated_data
        
        service=ProductCoordinatorService(user=request.user)
        #product=None
        
        try:
            product = service.create(
            name=data.get('name'),
            category=data.get('category'),
            keywords=data.get('keywords', []),
            basic_price=data.get('basic_price'),
            option=data.get('option'),
            product_photos=data.get('product_photos', []),
            info=data.get('info'),
            notice=data.get('notice'),
            period=data.get('period'),
            transaction_direct=data.get('transaction_direct'),
            transaction_package=data.get('transaction_package'),
            refund=data.get('refund'),
            )
            print('여기까지 정상 출력됨')
            
            if product is not None:
                return Response({
                'status' : 'success',
                'data' : {'id': product.id},
                },status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'status':'failure','message':'Product생성 실패',
                },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            # if product.product_photos:
            #     ProductPhotoService.process_photos(product=product, product_photos=product.product_photos)
            # else:
            #     print("product_photos가 none 입니다.")

        except Exception as e:
            print('오류 발생:', e)
            
            return Response({
                'status':'failure',
                'message':'서버 오류 발생',
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        #ProductPhotoService.process_photos(product=product, product_photos=product.product_photos)
        
        return Response({
            'status': 'success',
            'data' : {'id': product.id},
        }, status=status.HTTP_201_CREATED)
        
class ProductPhotoCreateApi(APIView):
    permission_classes=(AllowAny,)
    
    class ProductPhotoCreateInputSerializer(serializers.Serializer):
        image = serializers.ImageField()
    
    def post(self, request):
        serializers = self.ProductPhotoCreateInputSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        data = serializers.validated_data
        
        product_photo_url = ProductPhotoService.create(
            image=data.get('image'),
        )
        
        return Response({
            'status':'success',
            'data':{'location': product_photo_url},
        }, status = status.HTTP_201_CREATED)
        