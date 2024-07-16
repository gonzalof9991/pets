from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True, default=None)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()
        return self

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.updated_at = timezone.now()
        super().save(force_insert, force_update, using, update_fields)

    def update(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()
        return self


class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True, default=None)
    price = models.FloatField()
    stock = models.IntegerField()
    qualification = models.FloatField(blank=True, null=True, default=None)
    image = models.ImageField(upload_to="products/", blank=True, null=True, default=None)
    image_url = models.URLField(blank=True, null=True, default=None)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Rescued(BaseModel):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    race = models.CharField(max_length=255, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    direction = models.CharField(max_length=255, blank=True, null=True, default=None)
    image = models.ImageField(upload_to="products/", blank=True, null=True, default=None)
    image_url = models.URLField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True, default=None)
    image = models.ImageField(upload_to="products/", blank=True, null=True, default=None)
    image_url = models.URLField(blank=True, null=True, default=None)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Order(BaseModel):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    products = ArrayField(models.IntegerField())
    total = models.FloatField()


class User(BaseModel):
    email = models.EmailField()
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.email
