from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html
from django.utils.timezone import now


# Create your models here.

# category models

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/images/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tags(self):
        return format_html(
            '<img src="/media/{}" style="width:40px; height:40px; border-radius:50%" /> '.format(self.image))

    def __str__(self):
        return self.title


# Post model

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/images/')
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    def image_tags(self):
        return format_html(
            '<img src="/media/{}" style="width:40px; height:40px; border-radius:50%" /> '.format(self.image))

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username
