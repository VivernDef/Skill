from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import PerevalAdded
from rest_framework import generics
from .serializers import PerevalSerializer


class PerevalAPIList(generics.ListCreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer

    # def get(self, request):
    #     w = PerevalAdded.objects.all()
    #     return Response({'post': PerevalSerializer(w, many=True)})
    #
    # def post(self, request):
    #     serializer = PerevalSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     data = serializer.save()
    #     return Response({'status': 200, 'message':'Ожидайте модерации', 'id': data.id})

