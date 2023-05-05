from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView
from rest_framework.response import Response


from .models import PerevalAdded
from rest_framework import generics
from .serializers import PerevalSerializer, MountainCoordSerializer, PerevalSerializerUPdate


class PerevalAPIList(generics.ListCreateAPIView):
    """ Отобаржение всех статей """
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer

    def post(self, request):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
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


class PerevalAPIListView(generics.ListAPIView):
    """Фильтрация по email"""
    serializer_class = PerevalSerializer

    def get_queryset(self):
        queryset = PerevalAdded.objects.all()
        email = self.request.query_params.get('email')
        if email is not None:
            queryset = queryset.filter(user__email=email)
        return queryset


class PerevalAPIOne(RetrieveAPIView):
    """Отображение одной страницы"""
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer


class PerevalAPIUpdate(RetrieveUpdateAPIView):
    """Обновление страницы с ограничением"""
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializerUPdate

    def update(self, request, *args, **kwargs):
        submit_data = self.get_object()
        if submit_data.status != 'new':
            return Response({'state': 0, 'message': 'Администратор обрабатывает информацию'})
        else:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({'state': 1})
