from django.contrib.auth.models import User
from django.db import models
from board.models import Post


class Reply(models.Model):
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)