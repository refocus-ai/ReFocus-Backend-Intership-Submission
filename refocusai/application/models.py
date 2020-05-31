from django.db import JSONField, models
import uuid

# Create your models here.
class Company(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    #example_field = models.CharField(max_length=200)
    name = models.CharField(max_length=200) # name
    address = models.CharField(max_length=200) # address
    num_employees = models.IntegerField() # number of employees
    admin = models.OneToOneField(RefocusUser) # company has 1 admin user

class RefocusUser(models.Model):
    #example_field = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200) # first name
    last_name = models.CharField(max_length=200) # last name
    email_address = models.EmailField(max_length=200) # email address
    job_title = models.CharField(max_length=200) # job_title
    last_date = models.DateField() # date of last application use
    admin_user = models.BooleanField() # admin user
    company = models.ForeignKey(Company, ondelete=models.CASCADE) # many users 1 company
    permissions = models.ManyToManyField(Permissions) # users can have permissions

class Permissions(models.Model):
    #example_field = models.CharField(max_length=200)
    type = models.CharField(max_length=200) # permission type
    name = models.CharField(max_length=200) # name

class DataEntry(models.Model):
    #example_field = models.CharField(max_length=200)
    name = models.CharField(max_length=200) # name
    upload_date = models.DateField() # date which data was uploaded
    data = JSONField() # data (JSON)
    user = models.ForeignKey(RefocusUser, on_delete=models.CASCADE) # many entries 1 user
    permissions = models.ManyToManyField(Permissions, through='RefocusUser') # data entry has permissions which the user sets
