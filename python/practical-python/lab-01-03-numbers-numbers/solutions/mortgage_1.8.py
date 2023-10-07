# mortgage_1.8.py

# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000.0
total_paid = 0.0
months = 0

while principal > 0:
    months += 1
    if months <= 12:
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid += payment + extra_payment
    else:
        principal = principal * (1+rate/12) - payment
        total_paid += payment

print('Total paid:', total_paid)
print('Number of months:', months)