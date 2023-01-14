from django_filters import FilterSet, DateFilter, CharFilter, ModelChoiceFilter
from .models import Post, Author
from django import forms


class PostFilter(FilterSet):
    search_title = CharFilter(
        field_name='theme_news',
        label='Поиск темы',
        lookup_expr='icontains'
    )
    search_author = ModelChoiceFilter(
        empty_label='Выбор Автора',
        field_name='authors',
        label='Автор',
        queryset=Author.objects.all()
    )
    post_date__gt = DateFilter(
        field_name='date_joined',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Дата',
        lookup_expr='date__gte'
    )
