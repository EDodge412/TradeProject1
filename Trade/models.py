from django.db import models
from django.contrib.auth.models import User

LISTING_TYPE = (
    ('Online', 'Online'),
    ('In-Person', 'In-Person')
)


class listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    type = models.CharField(max_length=20, blank=False, choices=LISTING_TYPE)
    image = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self


class message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=600)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self


class payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    address = models.CharField(max_length=400)
    card_num = models.CharField(max_length=100)
    exp = models.CharField(max_length=10)
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return self
