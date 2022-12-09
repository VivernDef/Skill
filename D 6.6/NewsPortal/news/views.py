from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post


class PostList (ListView):
    model = Post
    ordering = '-date_joined'
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['next_sale'] = None
        return context


class PostInDetail (DetailView):
    model = Post
    template_name = 'post_show.html'
    context_object_name = 'post_show'
