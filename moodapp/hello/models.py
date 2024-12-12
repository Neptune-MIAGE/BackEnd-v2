from django.db import models

# Create your models here.
class HelloTest(models.Model):
    message = models.fields.CharField(max_length=20)