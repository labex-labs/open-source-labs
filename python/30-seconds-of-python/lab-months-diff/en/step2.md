# Creating the Month Difference Function

Now that we understand how to work with date objects and calculate the difference in days, let's create a function to calculate the difference in months.

In many applications, a month is approximated as 30 days. While this is not always accurate (months can have 28 to 31 days), it is a common simplification that works well for many business calculations.

Open your `month_difference.py` file and add this function below your existing code:

```python
def months_diff(start, end):
    """
    Calculate the difference in months between two dates.

    Args:
        start (date): The start date
        end (date): The end date

    Returns:
        int: The number of months between the dates (rounded up)
    """
    # Calculate the difference in days
    days_difference = (end - start).days

    # Convert days to months (assuming 30 days per month) and round up
    months = ceil(days_difference / 30)

    return months
```

Let's understand what this function does:

1. It takes two parameters: `start` and `end`, which are date objects
2. It calculates the difference in days between these dates
3. It divides by 30 to convert days to months
4. It uses `ceil()` to round up to the nearest integer
5. It returns the result as an integer

The `ceil()` function is used because in many business scenarios, even a partial month is counted as a full month for billing purposes.

To test our function, add the following code at the end of your file:

```python
# Test the months_diff function with our example dates
print(f"Months between {date1} and {date2}: {months_diff(date1, date2)}")

# Test with some other date pairs
print(f"Months between 2020-10-28 and 2020-11-25: {months_diff(date(2020, 10, 28), date(2020, 11, 25))}")
print(f"Months between 2020-12-15 and 2021-01-10: {months_diff(date(2020, 12, 15), date(2021, 01, 10))}")
```

Save your file and run it again:

```bash
python3 ~/project/month_difference.py
```

You should see output like:

```
Date 1: 2023-01-15
Date 2: 2023-03-20
Difference in days: 64
Months between 2023-01-15 and 2023-03-20: 3
Months between 2020-10-28 and 2020-11-25: 1
Months between 2020-12-15 and 2021-01-10: 1
```

Notice that:

- The 64 days between 2023-01-15 and 2023-03-20 is calculated as 3 months (64/30 = 2.13, rounded up to 3)
- The difference between October 28 and November 25 is calculated as 1 month
- The difference between December 15 and January 10 (across a year boundary) is also calculated as 1 month
