from django.db import models

class ProjectWebsite(models.Model):
    image = models.ImageField(upload_to='intro/images/')
    title = models.CharField(max_length=64)
    project_type = models.CharField(max_length=64)
    description = models.TextField()
    page_url = models.URLField()
    github_url = models.URLField()

    def __str__(self):
        return self.title

class ProjectWebpage(models.Model):
    image = models.ImageField(upload_to='intro/images/')
    title = models.CharField(max_length=64)
    project_type = models.CharField(max_length=64)
    description = models.TextField()
    page_url = models.URLField()
    github_url = models.URLField()

    def __str__(self):
        return self.title

class ProjectFunWebpage(models.Model):
    image = models.ImageField(upload_to='intro/images/')
    title = models.CharField(max_length=64)
    project_type = models.CharField(max_length=64)
    description = models.TextField()
    page_url = models.URLField()
    github_url = models.URLField()

    def __str__(self):
        return self.title
    