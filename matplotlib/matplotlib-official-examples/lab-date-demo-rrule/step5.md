# Set the dates and generate random data

You need to set the start and end dates and the delta, which represents the difference between each date. You also need to generate random data for the example.

```python
date1 = datetime.date(1952, 1, 1)
date2 = datetime.date(2004, 4, 12)
delta = datetime.timedelta(days=100)

dates = drange(date1, date2, delta)
s = np.random.rand(len(dates))
```
