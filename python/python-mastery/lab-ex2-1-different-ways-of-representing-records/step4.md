# Memory Use of Other Data Structures

Python has many different choices for representing data structures.
For example:

```python
# A tuple
row = (route, date, daytype, rides)

# A dictionary
row = {
    'route': route,
    'date': date,
    'daytype': daytype,
    'rides': rides,
}

# A class
class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# A named tuple
from collections import namedtuple
Row = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

# A class with __slots__
class Row:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides
```

Your task is as follows: Create different versions of the `read_rides()` function
that use each of these data structures to represent a single row of data.
Then, find out the resulting memory use of each option. Find out which
approach offers the most efficient storage if you were working with a lot
of data all at once.
