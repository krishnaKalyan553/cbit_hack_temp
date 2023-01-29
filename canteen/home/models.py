from django.db import models

# Create your models here.


class Person(models.Model):
    p_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)