
from django.urls import path
from .views import PostList, PostInDetail, PostCreate, PostEdit, PostDelete, PostCreateArticle, PostSearch

urlpatterns = [
    path('', PostList.as_view(), name='all_posts'),
    path('<int:pk>', PostInDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('article/', PostCreateArticle.as_view(), name='post_article'),
    path('<int:pk>/update', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('search/', PostSearch.as_view(), name='post_search')

]
