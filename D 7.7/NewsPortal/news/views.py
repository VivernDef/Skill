from datetime import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm


class PostList (ListView):
    model = Post
    ordering = '-date_joined'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['next_sale'] = None
        context['filterset'] = self.filterset
        return context


class PostInDetail (DetailView):
    model = Post
    template_name = 'post_show.html'
    context_object_name = 'post_show'


class PostCreate (CreateView):
    form_class = PostForm
    model = Post
    template_name = 'create.html'


class PostCreateArticle (CreateView):
    form_class = PostForm
    model = Post
    template_name = 'article.html'
    success_url = reverse_lazy('post_detail')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.choice_news = 'article'
        post.save()


class PostEdit (UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'create.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('all_posts')


class PostSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts_search'
    ordering = '-date_joined'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context




