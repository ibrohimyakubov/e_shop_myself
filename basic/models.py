from django.db import models


class Setting(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud emas'),
    )
    title = models.CharField(max_length=222)
    description = models.TextField(max_length=255)
    company = models.CharField(max_length=150)
    address = models.CharField(max_length=155, blank=True)
    phone = models.CharField(max_length=155, blank=True)
    email = models.CharField(max_length=155, blank=True)
    icon = models.ImageField(upload_to='media/images/', blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    twitter = models.CharField(max_length=155, blank=True)
    youtube = models.CharField(max_length=155, blank=True)
    aboutus = models.TextField(blank=True)
    contact = models.TextField(blank=True)

    status = models.CharField(max_length=10, choices=STATUS)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'setting'
        verbose_name_plural = 'settings'

    def __str__(self):
        return self.title


class Category(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud emas'),
    )
    title = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='media/category', blank=True)
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud emas'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=False)
    image = models.ImageField(upload_to='images/product', blank=False)
    price = models.FloatField()
    amount = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return self.title

