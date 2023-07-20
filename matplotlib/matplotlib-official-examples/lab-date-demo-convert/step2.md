# Define the dates and delta

Next, we will define the dates and delta values using the datetime library. The date range will be from March 2, 2000, to March 6, 2000, with a 6-hour interval. Copy and paste the following code:

```python
date1 = datetime.datetime(2000, 3, 2)
date2 = datetime.datetime(2000, 3, 6)
delta = datetime.timedelta(hours=6)
dates = drange(date1, date2, delta)
```
