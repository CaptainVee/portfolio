from django.contrib import admin
from .models import BlogPost
# Register your models here.


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
    )
    blog_post_fields = ('content',)