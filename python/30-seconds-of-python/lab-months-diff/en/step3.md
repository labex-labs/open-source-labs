# Testing with Various Date Scenarios

To better understand how our `months_diff` function works with different date scenarios, let's create a separate test file. This approach is common in software development to verify that our code works as expected.

Create a new file called `month_diff_test.py` in the `/home/labex/project` directory:

```python
from datetime import date
from month_difference import months_diff

# Test scenario 1: Dates in the same month
date1 = date(2023, 5, 5)
date2 = date(2023, 5, 25)
print(f"Same month: {months_diff(date1, date2)} month(s)")

# Test scenario 2: Consecutive months
date3 = date(2023, 6, 28)
date4 = date(2023, 7, 15)
print(f"Consecutive months: {months_diff(date3, date4)} month(s)")

# Test scenario 3: Dates crossing year boundary
date5 = date(2023, 12, 20)
date6 = date(2024, 1, 10)
print(f"Across years: {months_diff(date5, date6)} month(s)")

# Test scenario 4: Several months apart
date7 = date(2023, 3, 10)
date8 = date(2023, 9, 20)
print(f"Several months: {months_diff(date7, date8)} month(s)")

# Test scenario 5: Dates in reverse order (negative result)
print(f"Reverse order: {months_diff(date8, date7)} month(s)")

# Test scenario 6: Exact multiples of 30 days
date9 = date(2023, 1, 1)
date10 = date(2023, 1, 31)  # 30 days
date11 = date(2023, 3, 2)   # 60 days
print(f"30 days exactly: {months_diff(date9, date10)} month(s)")
print(f"60 days exactly: {months_diff(date9, date11)} month(s)")
```

Save this file and run it:

```bash
python3 ~/project/month_diff_test.py
```

You should see output similar to:

```
Same month: 1 month(s)
Consecutive months: 1 month(s)
Across years: 1 month(s)
Several months: 7 month(s)
Reverse order: -7 month(s)
30 days exactly: 1 month(s)
60 days exactly: 2 month(s)
```

Let's analyze these results:

1. **Same month**: Even within the same month, our function returns 1 month. This is because even a partial month is counted as a full month.

2. **Consecutive months**: For dates in consecutive months, the function returns 1 month.

3. **Across years**: For dates that cross the year boundary, the function still calculates correctly.

4. **Several months**: For dates that are several months apart, the function calculates the appropriate number of months.

5. **Reverse order**: When the end date is before the start date, we get a negative result, which makes sense for scenarios like calculating remaining time.

6. **Exact multiples**: For exactly 30 days, we get 1 month. For 60 days, we get 2 months. This confirms our function works as expected with exact multiples of our month definition.

Our `months_diff` function handles all these test cases correctly according to our definition of a month as 30 days.
