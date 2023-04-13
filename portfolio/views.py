from django.shortcuts import render
from .models import BlogPost
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
# Create your views here.


def index(request):
    return render(request, "portfolio/index.html", {"title": "Home"})



class BlogPostListView(ListView):
    model = BlogPost
    context_object_name = 'blog_posts'
    ordering = ['-created_at']
    paginate_by = 5


class BlogPostDetailView(DetailView):
    model = BlogPost
    context_object_name = 'blog_post'