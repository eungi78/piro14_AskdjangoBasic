from django.db import models

# Create your models here.


class Post(models.Model):
    author_name = models.TextField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    # post가 삭제되면 참조값 같이 삭제.
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
