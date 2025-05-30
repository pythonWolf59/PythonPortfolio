from django.contrib import admin

from users.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)  # Assuming Customer is defined in models.py
