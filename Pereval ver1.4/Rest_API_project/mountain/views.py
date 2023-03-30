from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import PerevalAdded
from rest_framework import generics
from .serializers import PerevalSerializer, MountainCoordSerializer


class PerevalAPIList(generics.ListCreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer

    def post(self, request):
        serializer = PerevalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response({'status': 200, 'message':'Ожидайте модерации', 'id': data.id})


class MountainCoordAPIList(generics.ListCreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = MountainCoordSerializer

    def post(self, request):
        serializer = MountainCoordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data=serializer.data, status=200)




    # def get(self, request):
    #     w = PerevalAdded.objects.all()
    #     return Response({'post': PerevalSerializer(w, many=True)})
    #
    # def post(self, request):
    #     serializer = PerevalSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     data = serializer.save()
    #     return Response({'status': 200, 'message':'Ожидайте модерации', 'id': data.id})

