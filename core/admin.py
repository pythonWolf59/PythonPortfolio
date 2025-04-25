from django.contrib import admin
from .models import Customer, LeaseContract, LoanContract

# Register your models here.
admin.site.register(Customer)
admin.site.register(LeaseContract)
admin.site.register(LoanContract)