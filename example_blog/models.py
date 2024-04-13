from django.db import models
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(
        max_length=50
    )
    body = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'pk': self.pk})
    
    def __str__(self):
        return f'{self.title}'