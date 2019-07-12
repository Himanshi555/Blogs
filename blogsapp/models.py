from django.db import models
from datetime import datetime
from django.urls import reverse


class Blog(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.TextField(max_length=2000)
    Image = models.ImageField(upload_to='Images/', null=True, blank=True)
    date_and_time = models.DateTimeField(default=datetime.today())

    def get_absolute_url(self):
        return reverse("bl:Detail_view", args=[self.pk])



class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    # reply = models.ForeignKey('Comment', on_delete=models.SET_NULL, null=True, related_name="replies")
    Name = models.CharField(max_length=200, null=True, blank=True)
    reply = models.ForeignKey('Comment', on_delete=models.SET_NULL, null=True, related_name="replies")
    comment = models.TextField()
    date_and_time = models.DateTimeField(auto_now_add=True)
