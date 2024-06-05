# Saving a lot of memory

In Exercise 2.1 you wrote a function `read_rides_as_dicts()` that read the CTA bus data into a list of dictionaries. Using it requires a lot of memory. For example, let's find the day on which the route 22 bus had the greatest ridership:

```python
>>> import tracemalloc
>>> tracemalloc.start()
>>> import readrides
>>> rows = readrides.read_rides_as_dicts('ctabus.csv')
>>> rt22 = [row for row in rows if row['route'] == '22']
>>> max(rt22, key=lambda row: row['rides'])
{'date': '06/11/2008', 'route': '22', 'daytype': 'W', 'rides': 26896}
>>> tracemalloc.get_traced_memory()
... look at result. Should be around 220MB
>>>
```

Now, let's try an example involving generators. Restart Python and try this:

```python
>>> # RESTART
>>> import tracemalloc
>>> tracemalloc.start()
>>> import csv
>>> f = open('ctabus.csv')
>>> f_csv = csv.reader(f)
>>> headers = next(f_csv)
>>> rows = (dict(zip(headers,row)) for row in f_csv)
>>> rt22 = (row for row in rows if row['route'] == '22')
>>> max(rt22, key=lambda row: int(row['rides']))
{'date': '06/11/2008', 'route': '22', 'daytype': 'W', 'rides': 26896}
>>> tracemalloc.get_traced_memory()
... look at result. Should be a LOT smaller than before
>>>
```

Keep in mind that you just processed the entire dataset as if it was stored as a sequence of dictionaries. Yet, nowhere did you actually create and store a list of dictionaries. Not all problems can be structured in this way, but if you can work with data in an iterative manner, generator expressions can save a huge amount of memory.
