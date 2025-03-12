# Optimizing Memory with Column-Oriented Data

Instead of storing each record as a separate dictionary (row-oriented), we can store data in columns to save memory. In this approach, we have separate lists for each attribute, where each list contains all values for that attribute.

1. Create a new Python file named `readrides.py` in your project directory:

```bash
cd ~/project
touch readrides.py
```

2. Open the file in the WebIDE editor and add the following code:

```python
# readrides.py
import csv
import sys
import tracemalloc

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

3. Now let's analyze why this approach should save memory. In the Python shell:

```python
import readrides
import tracemalloc

# Estimate memory for row-oriented approach
nrows = 577563     # Number of rows in original file
dict_overhead = 240  # Approximate dictionary overhead in bytes
row_memory = nrows * dict_overhead
print(f"Estimated memory for row-oriented data: {row_memory} bytes ({row_memory/1024/1024:.2f} MB)")

# Estimate memory for column-oriented approach
pointer_size = 8   # Size of a pointer in bytes on 64-bit systems
column_memory = nrows * 4 * pointer_size  # 4 columns with one pointer per entry
print(f"Estimated memory for column-oriented data: {column_memory} bytes ({column_memory/1024/1024:.2f} MB)")

# Estimate savings
savings = row_memory - column_memory
print(f"Estimated memory savings: {savings} bytes ({savings/1024/1024:.2f} MB)")
```

This calculation shows that the column-oriented approach should save around 120MB of memory compared to the row-oriented approach with dictionaries.

4. Let's verify this by measuring the actual memory usage with `tracemalloc`:

```python
# Start tracking memory
tracemalloc.start()

# Read the data
columns = readrides.read_rides_as_columns('ctabus.csv')

# Get current and peak memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current/1024/1024:.2f} MB")
print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

# Stop tracking memory
tracemalloc.stop()
```

The output will show you the actual memory usage of your column-oriented data structure. This should be significantly less than our theoretical estimate for the row-oriented approach.

The significant memory savings come from eliminating the overhead of thousands of dictionary objects. Each dictionary in Python has a fixed overhead regardless of how many items it contains. By using column-oriented storage, we only need a few lists instead of thousands of dictionaries.
