from tinymce import HTMLField
from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from django.urls import reverse
from PIL import Image

from reporter.models import Incidences, Counties

User = get_user_model()


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Asset(models.Model):
    image = models.ImageField(upload_to='assets')

    def save(self, *args, **kwargs):
        super(Asset, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 600 or img.width > 800:
            output_size = (600, 800)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    content = HTMLField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    point = models.ForeignKey(Incidences, on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(Counties, on_delete=models.SET_NULL, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='assets', null=True, blank=True)
    categories = models.ManyToManyField(Category)
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

        if self.thumbnail:
            img = Image.open(self.thumbnail.path)

            if img.height > 600 or img.width > 800:
                output_size = (600, 800)
                img.thumbnail(output_size)
                img.save(self.thumbnail.path)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'pk': self.pk
        })

    def get_update_url(self):
        return reverse('post-update', kwargs={
            'pk': self.pk
        })

    def get_delete_url(self):
        return reverse('post-delete', kwargs={
            'pk': self.pk
        })

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()