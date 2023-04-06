from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.views import APIView
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class SuvviewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Suv.objects.all()
    serializer_class = SuvSerializers

class AdminViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Admin.objects.all()
    serializer_class = AdminSerializers

class BuyurtmaviewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializers

class MijozViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializers

# class HaydovchiApiview(APIView):
#     def get(self, request):
#         haydovchi = Haydovchi.objects.all()
#         serializer = HaydovchiSerializers(haydovchi, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class HaydovchiViewset(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Haydovchi.objects.all()
    serializer_class = HaydovchiSerializers

