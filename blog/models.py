from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
