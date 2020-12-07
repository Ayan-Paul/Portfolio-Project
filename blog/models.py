from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=64)
    pub_date = models.DateField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return self.title