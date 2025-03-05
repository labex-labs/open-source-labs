# Creating a Practical Application: Subscription Calculator

Now that we have a reliable function for calculating month differences, let's apply it to a real-world scenario. We will create a subscription calculator that determines the cost of a service subscription between two dates.

Create a new file called `subscription_calculator.py` in the `/home/labex/project` directory:

```python
from datetime import date, timedelta
from month_difference import months_diff

def calculate_subscription_cost(start_date, end_date, monthly_fee):
    """
    Calculate the total cost of a subscription between two dates.

    Args:
        start_date (date): Subscription start date
        end_date (date): Subscription end date
        monthly_fee (float): Cost per month

    Returns:
        float: Total subscription cost
    """
    # Calculate number of months
    months = months_diff(start_date, end_date)

    # Calculate total cost
    total_cost = months * monthly_fee

    return total_cost

# Example: Calculate subscription cost for a streaming service
start = date(2023, 1, 15)  # Subscription starts January 15, 2023
end = date(2023, 8, 20)    # Ends August 20, 2023
monthly_cost = 9.99        # $9.99 per month

total = calculate_subscription_cost(start, end, monthly_cost)
print(f"Subscription period: {start} to {end}")
print(f"Monthly fee: ${monthly_cost:.2f}")
print(f"Total cost: ${total:.2f}")

# Compare with an annual plan
annual_cost = 99.99  # $99.99 per year
print(f"\nAnnual plan cost: ${annual_cost:.2f}")
print(f"Monthly plan for same period: ${total:.2f}")

if total > annual_cost:
    print(f"Savings with annual plan: ${total - annual_cost:.2f}")
else:
    print(f"Additional cost for annual plan: ${annual_cost - total:.2f}")

# Calculate cost for a trial period
today = date.today()
trial_end = today + timedelta(days=7)  # 7-day trial
trial_cost = calculate_subscription_cost(today, trial_end, monthly_cost)
print(f"\nOne-week trial period: {today} to {trial_end}")
print(f"Trial period cost: ${trial_cost:.2f}")
```

Save the file and run it:

```bash
python3 ~/project/subscription_calculator.py
```

You should see output similar to this (the trial dates will show your current date):

```
Subscription period: 2023-01-15 to 2023-08-20
Monthly fee: $9.99
Total cost: $79.92

Annual plan cost: $99.99
Monthly plan for same period: $79.92
Additional cost for annual plan: $20.07

One-week trial period: 2023-06-01 to 2023-06-08
Trial period cost: $9.99
```

This application demonstrates how our `months_diff` function can be used in a practical scenario:

1. We calculate the total cost of a subscription based on the number of months between two dates
2. We compare this cost with an annual plan to help a user decide which plan is more economical
3. We calculate the cost for a short trial period

Notice how even the 7-day trial gets charged as one full month in our model. This is because our function rounds up any partial month to a full month, which is common in subscription billing.

This type of calculation is frequently used in:

- Subscription services (streaming, software, memberships)
- Loan and mortgage calculations
- Rental agreements
- Project billing
