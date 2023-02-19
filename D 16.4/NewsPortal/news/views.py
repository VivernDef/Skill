from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Author, Category
from .filters import PostFilter
from .forms import PostForm

import logging

logger = logging.getLogger("django")


class PostList (ListView):
    logger.info("Hello LoG")
    model = Post
    ordering = '-date_joined'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['next_sale'] = None
      #  context['filterset'] = self.filterset
        return context


class PostInDetail (DetailView):
    model = Post
    template_name = 'post_show.html'
    context_object_name = 'post_show'


class PostCreate (LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    form_class = PostForm
    model = Post
    template_name = 'create.html'
    success_url = 'post_detail'
    permission_required = ('news.add_post', 'news.change_post',)


class PostCreateArticle (LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    form_class = PostForm
    model = Post
    template_name = 'article.html'
    success_url = reverse_lazy('post_detail')
    permission_required = ('news.add_post', 'news.change_post',)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.choice_news = 'article'
        post.save()


@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='Authors')
    if not request.user.groups.filter(name='Authors').exists():
        premium_group.user_set.add(user)
    return redirect('/posts/')


class PostEdit (LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'create.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('all_posts')


class PostSearch(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts_search'
    ordering = '-date_joined'
    paginate_by = 2
    success_url = reverse_lazy('all_posts')

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['is_not_authors'] = not self.request.user.groups.filter(name='Authors').exists()
        return context


class CategoryListV(PostList):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category_a = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(categorys=self.category_a).order_by('-date_joined')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category_a.subscribers.all()
        context['category_a'] = self.category_a
        return context

@login_required
def subscriber(request, pk):
    user = request.user
    category_b = Category.objects.get(id=pk)
    category_b.subscribers.add(user)

    mess = 'Вы подписались'
    return render(request, '/subscriber.html', {'category_b': category_b, 'mess': mess})




