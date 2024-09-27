from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated

from product.serializers import ProductSerializer

from core.models import Product
from core.permissions import IsManagerOrAssistant


class ProductAPIView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by("-id")
    authentication_classes = [authentication.TokenAuthentication]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsManagerOrAssistant]

        return super().get_permissions()
