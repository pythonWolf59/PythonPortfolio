from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Customer, LoanContract
from .serializers import CustomerSerializer, LoanContractSerializer

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

# Add your other viewsets here
class LoanContractViewSet(viewsets.ModelViewSet):
    ''' LoanContract viewset to manage loan contracts '''

    queryset = LoanContract.objects.all()
    serializer_class = LoanContractSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # Set the lookup field to 'email' instead of 'id'
    lookup_field = 'email'

    def get_object(self):
        email = self.kwargs.get('email') or self.kwargs.get('pk')  # supports both if needed
        return get_object_or_404(LoanContract, email=email)
    
    def perform_create(self, serializer):
        "Automatic interest rate calculation based on the loan amount and tenure"
        serializer.save()