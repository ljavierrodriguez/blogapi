from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    subtitle = models.CharField(max_length=300, blank=False, null=False)
    slug = models.CharField(max_length=200, blank=False, null=False, unique=True)
    content = models.TextField()
    featured_images = models.ImageField(upload_to="posts", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.user', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
