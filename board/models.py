from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

class PostImage(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)