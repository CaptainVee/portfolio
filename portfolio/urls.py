from django.urls import path
from .views import index, BlogPostDetailView, BlogPostListView

urlpatterns = [
path('', index, name='portfolio-home'),
path('blog-posts/', BlogPostListView.as_view(), name='blog-list'),
path('blog-post/<int:pk>/', BlogPostDetailView.as_view(), name='blog-post'),

]