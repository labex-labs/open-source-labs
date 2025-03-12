# Creating a Custom Container Class

While the column-oriented approach saves memory, it breaks compatibility with code that expects data to be in the form of a list of dictionaries. To solve this problem, we can create a custom container class that presents a row-oriented interface while storing data in a column-oriented format internally.

1. Open the `readrides.py` file in the WebIDE editor and add the following class:

```python
# Add this to readrides.py
from collections.abc import Sequence

class RideData(Sequence):
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
        return {'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]}

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])
```

2. Now, let's implement a function that reads the bus ride data into our custom container:

```python
# Add this to readrides.py
def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts, but use our custom container
    '''
    records = RideData()
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
                'rides': rides
            }
            records.append(record)
    return records
```

This function creates a `RideData` object and populates it with data from the CSV file. The key aspect is that it maintains the same interface as a list of dictionaries, but internally stores the data in columns.

3. Let's test our custom container in the Python shell:

```python
import readrides

# Read the data using our custom container
rows = readrides.read_rides_as_dicts('ctabus.csv')

# Check the type of the returned object
type(rows)  # Should be readrides.RideData

# Check the length
len(rows)   # Should be 577563

# Access individual records
rows[0]     # Should return a dictionary for the first record
rows[1]     # Should return a dictionary for the second record
rows[2]     # Should return a dictionary for the third record
```

Our custom container successfully implements the Sequence interface, meaning it behaves like a list. You can use `len()` to get the number of records and use indexing to access individual records. Each record appears to be a dictionary, even though the data is stored in columns internally.

The advantage of this approach is that existing code that expects a list of dictionaries will continue to work with our custom container without modification, but the memory usage is much lower.

4. Let's measure the memory usage of our custom container:

```python
import tracemalloc

tracemalloc.start()
rows = readrides.read_rides_as_dicts('ctabus.csv')
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current/1024/1024:.2f} MB")
print(f"Peak memory usage: {peak/1024/1024:.2f} MB")
tracemalloc.stop()
```

You should see that the memory usage is similar to the column-oriented approach, which is much lower than a list of dictionaries would be.
