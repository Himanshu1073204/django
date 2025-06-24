
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100, default="admin")
    created_at = models.DateTimeField(auto_now_add=True)
    related_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


