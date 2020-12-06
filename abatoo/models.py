from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Region(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('abatoo:detail', args=[self.pk])


class Comment(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80, default='Anonymous')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.region}'