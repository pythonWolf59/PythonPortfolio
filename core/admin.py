from django.contrib import admin
from .models import Customer, LoanContract


#Approve or Reject Loan Contract via Admin Interface
class LoanContractAdmin(admin.ModelAdmin):
    list_display = ('customer', 'full_name', 'email', 'total_payable', 'loan_status', 'created_at')
    list_filter = ('loan_status', 'customer__customer_type')
    search_fields = ('full_name', 'email', 'customer__name')
    actions = ['approve_loans', 'reject_loans']

    def approve_loans(self, request, queryset):
        queryset.update(loan_status='active')
        self.message_user(request, "Selected loans have been approved.")

    def reject_loans(self, request, queryset):
        queryset.update(loan_status='defaulted')
        self.message_user(request, "Selected loans have been rejected.")
    
    approve_loans.short_description = "Approve selected loans"
    reject_loans.short_description = "Reject selected loans"

# Register your models here.
admin.site.register(Customer)
admin.site.register(LoanContract, LoanContractAdmin)
