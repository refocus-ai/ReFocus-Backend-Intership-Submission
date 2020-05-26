from django.db import models
import uuid

# Create your models here.
class Company(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    example_field = models.CharField(max_length=200)

class RefocusUser(models.Model):
    example_field = models.CharField(max_length=200)

class Permissions(models.Model):
    example_field = models.CharField(max_length=200)

class DataEntry(models.Model):
    example_field = models.CharField(max_length=200)