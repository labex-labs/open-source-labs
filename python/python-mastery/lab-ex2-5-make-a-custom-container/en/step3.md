# Changing Your Orientation (to Columns)

You can often save a lot of memory if you change your view of data. For example, what happens if you read all of the bus data into a columns using this function?

```python
# readrides.py

...

def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)
```

In theory, this function should save a lot of memory. Let's analyze it before trying it.

First, the datafile contained 577563 rows of data where each row contained four values. If each row is stored as a dictionary, then those dictionaries are minimally 240 bytes in size.

```python
>>> nrows = 577563     # Number of rows in original file
>>> nrows * 240
138615120
>>>
```

So, that's 138MB just for the dictionaries themselves. This does not include any of the values actually stored in the dictionaries.

By switching to columns, the data is stored in 4 separate lists.\
Each list requires 8 bytes per item to store a pointer. So, here's a rough estimate of the list requirements:

```python
>>> nrows * 4 * 8
18482016
>>>
```

That's about 18MB in list overhead. So, switching to a column orientation should save about 120MB of memory solely from eliminating all of the extra information that needs to be stored in dictionaries.

Try using this function to read the bus data and look at the memory use.

```python
>>> import tracemalloc
>>> tracemalloc.start()
>>> columns = read_rides_as_columns('ctabus.csv')
>>> tracemalloc.get_traced_memory()
... look at the result ...
>>>
```

Does the result reflect the expected savings in memory from our rough calculations above?
