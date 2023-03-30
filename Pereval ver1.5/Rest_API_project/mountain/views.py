
from rest_framework.response import Response


from .models import PerevalAdded, Tourist
from rest_framework import generics
from .serializers import PerevalSerializer, MountainCoordSerializer


class PerevalAPIList(generics.ListCreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer

    def post(self, request):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            data = serializer.save()
            return Response({'status': 200, 'message':'Ожидайте модерации', 'id': data.id})
        elif not serializer.is_valid():
            return Response({'status': 400, 'message':'Не все поля введены'})
        else:
            return Response({'status': 500, 'message': 'Сервер отдыхает'})


class MountainCoordAPIList(generics.ListCreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = MountainCoordSerializer

    def post(self, request):
        serializer = MountainCoordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data=serializer.data, status=200)


