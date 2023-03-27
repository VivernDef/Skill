from django.shortcuts import render
from django.views.generic import ListView

from .models import PerevalAdded


class PerevalAddedList(ListView):
    model = PerevalAdded
    template_name = 'main.html'
    context_object_name = 'Pereval'
