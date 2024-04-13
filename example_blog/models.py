from django.db import models

class BlogPost(models.Model):
    title = models.CharField(
        max_length=50
    )
    body = models.TextField()