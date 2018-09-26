from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=120)
    category_img = models.ImageField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=3, max_digits=10)
    description = models.TextField()
    img = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_purchase = models.DateTimeField(auto_now=False)
    product = models.ManyToManyField(Product, through='ProductItem')


class ProductItem(models.Model):
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)


class GetingUsersEmails(models.Model):
    user_email = models.CharField(max_length=200)
    registerd_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_email
