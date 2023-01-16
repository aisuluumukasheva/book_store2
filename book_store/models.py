from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()

class Book(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    published = models.DateTimeField()
