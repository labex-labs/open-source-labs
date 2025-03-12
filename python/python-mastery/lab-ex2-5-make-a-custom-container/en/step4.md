# Creating a Custom Container Class

In data processing, the column-oriented approach is great for saving memory. However, it can cause issues when your existing code expects data to be in the form of a list of dictionaries. To solve this problem, we'll create a custom container class. This class will present a row-oriented interface, which means it will look and act like a list of dictionaries to your code. But internally, it will store data in a column-oriented format, helping us save memory.

1. First, open the `readrides.py` file in the WebIDE editor. We're going to add a new class to this file. This class will be the foundation of our custom container.

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

In this code, we define a class named `RideData` that inherits from `Sequence`. The `__init__` method initializes four empty lists, each representing a column of data. The `__len__` method returns the length of the container, which is the same as the length of the `routes` list. The `__getitem__` method allows us to access a specific record by index, returning it as a dictionary. The `append` method adds a new record to the container by appending values to each column list.

2. Now, we need a function to read the bus ride data into our custom container. Add the following function to the `readrides.py` file.

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

This function creates an instance of the `RideData` class and populates it with data from the CSV file. It reads each row from the file, extracts the relevant information, creates a dictionary for each record, and then appends it to the `RideData` container. The key thing is that it maintains the same interface as a list of dictionaries, but internally stores the data in columns.

3. Let's test our custom container in the Python shell. This will help us verify that it works as expected.

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

Our custom container successfully implements the Sequence interface, which means it behaves like a list. You can use the `len()` function to get the number of records in the container, and you can use indexing to access individual records. Each record appears to be a dictionary, even though the data is stored in columns internally. This is great because existing code that expects a list of dictionaries will continue to work with our custom container without any modification.

4. Finally, let's measure the memory usage of our custom container. This will show us how much memory we're saving compared to a list of dictionaries.

```python
import tracemalloc

tracemalloc.start()
rows = readrides.read_rides_as_dicts('ctabus.csv')
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current/1024/1024:.2f} MB")
print(f"Peak memory usage: {peak/1024/1024:.2f} MB")
tracemalloc.stop()
```

When you run this code, you should see that the memory usage is similar to the column-oriented approach, which is much lower than what a list of dictionaries would use. This demonstrates the advantage of our custom container in terms of memory efficiency.
