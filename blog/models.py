from django.db import models
from django.conf import settings

# Create your models here.

class Tag(models.Model):
    value = models.TextField(max_length=100)

    def _str_(self):
        return self.value


class Post(models.Model):
    Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now = True)
    published_at = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    summary = models.TextField(max_length=150)
    content = models.TextField
    tag = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return self.Author