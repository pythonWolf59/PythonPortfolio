from rest_framework import serializers
from .models import Customer, EMIPayment, LoanContract

# This serializer is used to convert the Customer model instances into JSON format and vice versa.
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'  # Include all fields in the model

class LoanContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanContract
        fields = '__all__'

class EMIPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EMIPayment
        fields = '__all__'

