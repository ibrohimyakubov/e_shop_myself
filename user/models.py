from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class Profile(models.Model):
    CITY = [
        ('Tashkent', 'Tashkent'),
        ('America', 'America'),
    ]
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio...", max_length=400)
    email = models.EmailField(max_length=300, blank=True)
    country = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/user_image', blank=True)

    def __str__(self):
        return self.user.username

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
