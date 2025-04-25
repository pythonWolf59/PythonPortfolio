from django.db import models
from django.conf import settings

# Create your models here.

# We will create a model for managing Customer information
class Customer(models.Model):

    CUSTOMER_TYPE_CHOICES = [
        ('individual', 'Individual'),
        ('corporate', 'Corporate'),
    ]

    name = models.CharField(max_length=255)
    customer_type = models.CharField(max_length=20, choices=CUSTOMER_TYPE_CHOICES)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

# Now we will create a model for managing Loan of the customer
class LoanContract(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('closed', 'Closed'),
        ('overdue', 'Overdue'),
        ('defaulted', 'Defaulted'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='loan_contracts')
    principal_amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)  # as percentage
    term_months = models.IntegerField()
    payment_frequency = models.CharField(max_length=20, default='monthly')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    start_date = models.DateField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Loan #{self.id} for {self.customer.name}"

# Model for Lease Contract
class LeaseContract(models.Model):
    ASSET_TYPE_CHOICES = [
        ('vehicle', 'Vehicle'),
        ('equipment', 'Equipment'),
        ('property', 'Property'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='lease_contracts')
    asset_description = models.TextField()
    asset_type = models.CharField(max_length=20, choices=ASSET_TYPE_CHOICES)
    lease_term_months = models.IntegerField()
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    buyout_option = models.BooleanField(default=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lease #{self.id} for {self.customer.name}"

