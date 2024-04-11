from django.urls import path
from apps.posts import views

urlpatterns = [
    path('post/', views.PostList.as_view()),
    path('post/<uuid:pk>/', views.PostDetail.as_view()),
    path('comment/', views.CommentList.as_view()),
    path('comment/<uuid:pk>/', views.CommentDetail.as_view()),
]
