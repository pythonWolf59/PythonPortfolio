from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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
    
    REPAYMENT_FREQUENCY_CHOICES = [
        ('weekly', 'Weekly'),
        ('biweekly', 'Bi-Weekly'),
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
    ]

    LOAN_STATUS_CHOICES = [
        ('pending_approval', 'Approval Pending'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('defaulted', 'Defaulted'),
    ]

    LOAN_PURPOSE_CHOICES = [
        ('personal', 'Personal'),
        ('business', 'Business'),
        ('education', 'Education'),
        ('home_improvement', 'Home Improvement'),
        ('debt_consolidation', 'Debt Consolidation'),
        ('auto', 'Auto'),
        ('medical', 'Medical'),
        ('vacation', 'Vacation'),
        ('wedding', 'Wedding'),
        ('other', 'Other'),
    ]

    # Create table for LoanContract
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='loans')
    full_name = models.CharField(max_length=255, blank=False)   #Mandatory Field
    email = models.EmailField(blank=False)  #Mandatory Field
    address = models.TextField(blank=False) #Mandatory Field
    phone = models.CharField(max_length=15,blank=True)

    # Loan Details
    principal_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=False)  #Mandatory Field
    interest_rate = models.FloatField(default=0.0)
    total_payable = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    tenure_months = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(84)]
    )
    payment_option = models.CharField(max_length=25, choices=REPAYMENT_FREQUENCY_CHOICES, default='monthly')
    loan_status = models.CharField(max_length=25, choices=LOAN_STATUS_CHOICES, default='pending_approval')
    loan_purpose = models.CharField(max_length=25, choices=LOAN_PURPOSE_CHOICES, default='personal')
    is_islamic = models.BooleanField(default=False)
    markup_rate = models.FloatField(null=True, blank=True)  # Only used for Islamic loans

    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)  # Admin/Manager will approve

        # File Uploads (media)
    passport_or_nid = models.FileField(upload_to='documents/id/', null=True, blank=True)
    bank_statement = models.FileField(upload_to='documents/bank_statements/', null=True, blank=True)
    account_certificate = models.FileField(upload_to='documents/account_certificates/', null=True, blank=True)
    stamp_paper_signed = models.FileField(upload_to='documents/stamp_papers/', null=True, blank=True)


    def __str__(self):
        return f"{self.customer.name} - Loan #{self.id}"
    


class InstallmentSchedule(models.Model):

    '''
    This model will be used to manage the installment schedule for each loan contract.
    When a customer takes a loan, the system will automatically generate an installment schedule based on the loan details.
    So say if a customer takes a loan of 1000 with 4 weekly installments, 
    this class will create 4 rows associated with that specific loan contract.
    '''

    loan_contract = models.ForeignKey('LoanContract', on_delete=models.CASCADE, related_name='installments')
    
    installment_number = models.PositiveIntegerField()
    "A unique number for each installment"
    
    due_date = models.DateField()
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_paid = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        '''
        This class will make sure that no duplicate installments are created for one loan.
        also when we will fetch the installments for a loan, it will order them by due date.
        '''
        unique_together = ('loan_contract', 'installment_number')
        ordering = ['due_date']

    def __str__(self):
        return f"Installment {self.installment_number} for Loan #{self.loan_contract.id}"