from django.db import models
from django.utils import timezone
from django.urls import reverse
from django_quill.fields import QuillField
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = QuillField(blank=True, null=True)
    # content = RichTextField(blank=True,null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk' : self.pk})