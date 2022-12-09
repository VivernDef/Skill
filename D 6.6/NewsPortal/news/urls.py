
from django.urls import path
from .views import PostList, PostInDetail

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostInDetail.as_view()),
]
