# A List of Tuples

In practice, you might read the data into a list and convert each line
into some other data structure. Here is a program `readrides.py` that
reads the entire file into a list of tuples using the `csv` module:

```python
# readrides.py

import csv

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_tuples('Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
```

Run this program using `python3 -i readrides.py` and look at the
resulting contents of `rows`. You should get a list of tuples like
this:

```python
>>> len(rows)
577563
>>> rows[0]
('3', '01/01/2001', 'U', 7354)
>>> rows[1]
('4', '01/01/2001', 'U', 9288)
```

Look at the resulting memory use. It should be substantially higher
than in part (b).
