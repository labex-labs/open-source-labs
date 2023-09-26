# Exercise 1.8: Extra payments

Suppose Dave pays an extra \$1000/month for the first 12 months of the mortgage?

Modify the program to incorporate this extra payment and have it print the total amount paid along with the number of months required.

When you run the new program, it should report a total payment of `929965.6199999959` over 342 months.

Here is a solution:

```python
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment = 1000.0  
months_with_extra_payment = 12  

months = 0  

while principal > 0:
    months += 1
    if months <= months_with_extra_payment:
        principal = principal * (1 + rate / 12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment

print('Total paid:', total_paid)
print('Number of months:', months)
```