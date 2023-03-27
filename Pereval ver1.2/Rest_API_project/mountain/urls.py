from django.urls import path

from .views import PerevalAddedList

urlpatterns = [
    path('main', PerevalAddedList.as_view(), name='all_pereval'),
]
