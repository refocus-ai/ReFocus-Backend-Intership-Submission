from django.db import models
from django.utils import timezone
import uuid

YES = "Yes"
NO = "No"
admin_choice = [
    (YES, "Yes"),
    (NO, "No"),
]

# Create your models here.


class Company(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    address = models.CharField(max_length=200, default=uuid.uuid4)
    number = models.IntegerField(default=uuid.uuid4())

    def __str__(self):
        return self.id


class RefocusUser(models.Model):
    adminUser = models.OneToOneField(Company, related_name="admin", on_delete=models.CASCADE, choices=admin_choice,
                                     default=uuid.uuid4)
    user = models.ForeignKey(Company, related_name="user", on_delete=models.CASCADE, default=uuid.uuid4)
    firstName = models.CharField(max_length=32, default=uuid.uuid4)
    lastName = models.CharField(max_length=32, default=uuid.uuid4)
    emailAdd = models.EmailField(default=uuid.uuid4)
    jobTitle = models.TextField(default=uuid.uuid4)
    dataUse = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.firstName, self.lastName


class Permissions(models.Model):
    permission = models.ForeignKey(RefocusUser, on_delete=models.CASCADE, default=uuid.uuid4)
    permissionType = models.CharField(max_length=32, default=uuid.uuid4())
    permissionName = models.TextField(default=uuid.uuid4())

    def __str__(self):
        return self.permissionName


class DataEntry(models.Model):
    entryName = models.CharField(max_length=32, default=uuid.uuid4())
    entryDate = models.DateTimeField(default=timezone.now())
    entryFile = models.FilePathField(default=uuid.uuid4())
    entryUser = models.OneToOneField(RefocusUser, related_name="ReFocusUser", on_delete=models.CASCADE, default=uuid.uuid4)
    entryPermission = models.ForeignKey(Permissions, related_name="Permission", on_delete=models.CASCADE, default=uuid.uuid4)

    def __str__(self):
        return self.entryName, self.entryFile



