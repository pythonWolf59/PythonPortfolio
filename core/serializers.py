import decimal
from rest_framework import serializers
from .models import Customer, LoanContract

# This serializer is used to convert the Customer model instances into JSON format and vice versa.
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'  # Include all fields in the model

class LoanContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanContract
        fields = '__all__'  # Include all fields in the model
        read_only_fields = ['loan_status', 'approved', 'total_payable', 'interest_rate', 'loan_date']
        # These fields are set to read-only because we don't want them to be updated via the API

    def create(self, validated_data):
        principal_amount = validated_data['principal_amount']  # this is Decimal
        markup_rate = validated_data.get('markup_rate') or 0.0  # float or None

        # Convert markup_rate to Decimal
        markup_rate_decimal = decimal.Decimal(str(markup_rate))

        total_payable = principal_amount * (decimal.Decimal('1') + markup_rate_decimal / decimal.Decimal('100'))

        # Then save total_payable in validated_data or use directly
        validated_data['total_payable'] = total_payable.quantize(decimal.Decimal('0.01'))

        return super().create(validated_data)

    def _calculate_interest_rate(self, tenure, payment_option):
        """
        Calculates interest rate based on tenure and repayment frequency.
        Longer tenure = higher base rate.
        Frequent payments = discount; infrequent = penalty.
        """

        # 1. Base rate based on tenure (months)
        if tenure <= 6:
            base_rate = 5.0
        elif tenure <= 12:
            base_rate = 8.0
        elif tenure <= 24:
            base_rate = 11.0
        elif tenure <= 36:
            base_rate = 13.0
        elif tenure <= 60:
            base_rate = 15.0
        else:
            base_rate = 18.0  # More than 5 years

        # 2. Adjust based on repayment frequency
        frequency_modifier = {
            'weekly': -0.90,
            'biweekly': -0.75,
            'monthly': 0.0,
            'quarterly': +1.0,
        }

        modifier = frequency_modifier.get(payment_option, 0.0)
        interest_rate = base_rate + modifier

        # 3. Optional cap (e.g., max 22%)
        return min(round(interest_rate, 2), 22.0)

