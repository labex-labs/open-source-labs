# Optimizing Memory with Column-Oriented Data

In traditional data storage, we often store each record as a separate dictionary, which is called a row-oriented approach. However, this method can consume a significant amount of memory. An alternative way is to store data in columns. In the column-oriented approach, we create separate lists for each attribute, and each list holds all the values for that specific attribute. This can help us save memory.

1. First, you need to create a new Python file in your project directory. This file will contain the code for reading data in a column-oriented way. Name the file `readrides.py`. You can use the following commands in the terminal to achieve this:

```bash
cd ~/project
touch readrides.py
```

The `cd ~/project` command changes the current directory to your project directory, and the `touch readrides.py` command creates a new empty file named `readrides.py`.

2. Next, open the `readrides.py` file in the WebIDE editor. Then, add the following Python code to the file. This code defines a function `read_rides_as_columns` that reads bus ride data from a CSV file and stores it in four separate lists, each representing a column of data.

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

In this code, we first import the necessary modules `csv`, `sys`, and `tracemalloc`. The `csv` module is used to read CSV files, `sys` can be used for system-related operations (although not used in this function), and `tracemalloc` is used for memory profiling. Inside the function, we initialize four empty lists to store different columns of data. Then, we open the file, skip the header row, and iterate through each row in the file, appending the corresponding values to the appropriate lists. Finally, we return a dictionary containing these four lists.

3. Now, let's analyze why the column-oriented approach can save memory. We'll do this in the Python shell. Run the following code:

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

In this code, we first import the `readrides` module we just created and the `tracemalloc` module. Then, we estimate the memory usage for the row-oriented approach. We assume that each dictionary has an overhead of 240 bytes, and we multiply this by the number of rows in the original file to get the total memory usage for the row-oriented data. For the column-oriented approach, we assume that on a 64-bit system, each pointer takes 8 bytes. Since we have 4 columns and one pointer per entry, we calculate the total memory usage for the column-oriented data. Finally, we calculate the memory savings by subtracting the column-oriented memory usage from the row-oriented memory usage.

This calculation shows that the column-oriented approach should save around 120MB of memory compared to the row-oriented approach with dictionaries.

4. Let's verify this by measuring the actual memory usage with the `tracemalloc` module. Run the following code:

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

In this code, we first start tracking memory using `tracemalloc.start()`. Then, we call the `read_rides_as_columns` function to read the data from the `ctabus.csv` file. After that, we use `tracemalloc.get_traced_memory()` to get the current and peak memory usage. Finally, we stop tracking memory using `tracemalloc.stop()`.

The output will show you the actual memory usage of your column-oriented data structure. This should be significantly less than our theoretical estimate for the row-oriented approach.

The significant memory savings come from eliminating the overhead of thousands of dictionary objects. Each dictionary in Python has a fixed overhead regardless of how many items it contains. By using column-oriented storage, we only need a few lists instead of thousands of dictionaries.
