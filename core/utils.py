from dateutil.relativedelta import relativedelta
from decimal import Decimal

def calculate_emi(principal, annual_rate, term_months):
    r = Decimal(annual_rate) / 100 / 12
    emi = Decimal(principal * r * ((1 + r) ** term_months) / (((1 + r) ** term_months) - 1))
    return round(emi, 2)

def generate_emi_schedule(loan):
    from .models import EMIPayment
    emi_amount = calculate_emi(loan.principal_amount, loan.interest_rate, loan.term_months)
    for i in range(loan.term_months):
        due_date = loan.start_date + relativedelta(months=i)
        EMIPayment.objects.create(loan=loan, due_date=due_date, amount_due=emi_amount)