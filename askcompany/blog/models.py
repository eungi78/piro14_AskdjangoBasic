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


# Post.objects.all().count() --> 0
# post1 = Post.objects.create(author_name="author1", title="title1", content="content1")
# Comment.objects.all().count() --> 0
# Comment.objects.create(post=post1, message="django")
# Comment.objects.create(post=post1, message="fucking")
# Comment.objects.create(post=post1, message="hard")
# Comment.objects.all().count()
# post1.comment_set.all()
# Comment.objects.filter(post=post1)
