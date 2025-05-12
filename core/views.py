from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Customer, LoanContract, EMIPayment, LeaseContract
from .serializers import CustomerSerializer, LoanContractSerializer, EMIPaymentSerializer
from .utils import generate_emi_schedule
from datetime import date

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # Set the lookup field to 'email' instead of 'id'
    lookup_field = 'email'

    def get_queryset(self):
        # Optionally filter by email if needed (for other methods)
        return Customer.objects.all()

    def update(self, request, *args, **kwargs):
        # Get customer by email
        email = kwargs.get('email')
        try:
            customer = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return Response({"detail": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)

        # Update the customer data using the provided serializer
        serializer = self.get_serializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        # Get customer by email
        email = kwargs.get('email')
        try:
            customer = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return Response({"detail": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)

        # Delete the customer
        customer.delete()
        return Response({"detail": "Customer deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

class LoanContractViewSet(viewsets.ModelViewSet):
    queryset = LoanContract.objects.all()
    serializer_class = LoanContractSerializer

    @action(detail=True, methods=['post'])
    def disburse(self, request, pk=None):
        loan = self.get_object()

        # Only allow disbursement from 'draft' or 'active'
        if loan.status in ['draft', 'active']:
            if not loan.start_date:
                loan.start_date = date.today()

            loan.status = 'disbursed'
            loan.save()

            # Generate EMI schedule (this must be implemented)
            generate_emi_schedule(loan)

            return Response({"status": "Loan disbursed and EMI schedule created."})

        return Response({"detail": "Loan cannot be disbursed from its current state."}, status=400)


class EMIPaymentViewSet(viewsets.ModelViewSet):
    queryset = EMIPayment.objects.all()
    serializer_class = EMIPaymentSerializer

    @action(detail=True, methods=['post'])
    def mark_paid(self, request, pk=None):
        payment = self.get_object()
        if payment.status != 'paid':
            payment.status = 'paid'
            payment.amount_paid = payment.amount_due
            payment.payment_date = date.today()
            payment.save()
            return Response({"status": "EMI marked as paid"})
        return Response({"detail": "Already paid"}, status=400)