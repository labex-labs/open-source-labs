# Making a Custom Container - The Great Fake Out

Storing the data in columns offers a much better memory savings, but the data is now rather weird to work with. In fact, none of our earlier analysis code from Exercise 2.2 can work with columns. The reason everything is broken is that you've broken the data abstraction that was used in earlier exercises--namely the assumption that data is stored as a list of dictionaries.

This can be fixed if you're willing to make a custom container object that "fakes" it. Let's do that.

The earlier analysis code assumes the data is stored in a sequence of records. Each record is represented as a dictionary. Let's start by making a new "Sequence" class. In this class, we store the four columns of data that were being using in the `read_rides_as_columns()` function.

```python
# readrides.py

from collections.abc import Sequence

...

class RideData(Sequence):
    def __init__(self):
        self.routes = []      # Columns
        self.dates = []
        self.daytypes = []
        self.numrides = []
```

Try creating a `RideData` instance. You'll find that it fails with an error message like this:

```python
>>> records = RideData()
Traceback (most recent call last):
...
TypeError: Can't instantiate abstract class RideData with abstract methods __getitem__, __len__
>>>
```

Carefully read the error message. It tells us what we need to implement. Let's add a `__len__()` and `__getitem__()` method. In the `__getitem__()` method, we'll make a dictionary. In addition, we'll create an `append()` method that takes a dictionary and unpacks it into 4 separate `append()` operations.

```python
# readrides.py
...

class RideData(collections.Sequence):
    def __init__(self):
        # Each value is a list with all of the values (a column)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        return { 'route': self.routes[index],
                 'date': self.dates[index],
                 'daytype': self.daytypes[index],
                 'rides': self.numrides[index] }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])
```

If you've done this correctly, you should be able to drop this object into the previously written `read_rides_as_dicts()` function. It involves changing only one line of code:

```python
# readrides.py
...

def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts
    '''
    records = RideData()      # <--- CHANGE THIS
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides' : rides
                }
            records.append(record)
    return records
```

If you've done this right, old code should work exactly as it did before. For example:

```python
>>> rows = readrides.read_rides_as_dicts('ctabus.csv')
>>> rows
<readrides.RideData object at 0x10f5054a8>
>>> len(rows)
577563
>>> rows[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> rows[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>> rows[2]
{'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048}
>>>
```

Run your earlier CTA code from Exercise 2.2. It should work without modification, but use substantially less memory.
