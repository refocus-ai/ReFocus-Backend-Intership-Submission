from django.contrib import admin
from .models import Company, RefocusUser, Permissions, DataEntry

# Register your models here.
admin.site.register(Company) # company registered
admin.site.register(RefocusUser) # user registered
admin.site.register(Permissions) # permission registered
admin.site.register(DataEntry) # data entry registered
