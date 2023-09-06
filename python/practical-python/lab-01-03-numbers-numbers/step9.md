# Exercise 1.9: Making an Extra Payment Calculator

Modify the program so that extra payment information can be more generally handled. Make it so that the user can set these variables:

```python
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
```

Make the program look at these variables and calculate the total paid appropriately.

How much will Dave pay if he pays an extra \$1000/month for 4 years starting after the first five years have already been paid?

Here is a solution:

```python
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

months = 0
while principal > 0:
    months += 1
    if extra_payment_start_month <= months <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment

print('Total paid:', total_paid)
```