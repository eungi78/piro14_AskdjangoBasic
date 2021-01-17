from django.db import models
from django.urls import reverse
from askcompany.utils import uuid_upload_to
# from django.conf import settings


class Item(models.Model):
    name = models.CharField(max_length=100, validators=[])
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    photo = models.ImageField(blank=True, upload_to=uuid_upload_to)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<{self.pk}> {self.name}'

    def get_absolute_url(self):
        return reverse('shop:item_detail', kwargs={'pk': self.pk})


# class Profile(models.Model):
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     blog_url = models.URLField(blank=True)


# class Post(models.Model):
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(allow_unicode=True)  # 한글을 지원하기 위함
#     desc = models.TextField(blank=True)
#     image = models.ImageField(blank=True)
#     comment_count = models.PositiveIntegerField(default=0)
#     tag_set = models.ManyToManyField('Tag', blank=True)
#     is_publish = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Comment(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     post = models.ForeignKey(POST, on_delete=models.CASCADE)
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Tag(models.Model):
#     name = models.CharField(max_length=50, unique=True)
