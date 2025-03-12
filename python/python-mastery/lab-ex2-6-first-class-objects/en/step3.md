# Exploring Python's Memory Model

Python's memory model influences how objects are stored and referenced. In this step, we'll explore how string objects in particular are handled, and how we can optimize memory usage for large datasets.

## String Repetition in Datasets

The CTA bus data contains repeated values, such as route names. Let's examine how many unique route strings are in the dataset.

Open a Python interpreter:

```bash
python3
```

Load the CTA bus data and find the unique routes:

```python
import reader
rows = reader.read_csv_as_dicts('ctabus.csv', [str, str, str, int])

# Find unique route names
routes = {row['route'] for row in rows}
print(f"Number of unique route names: {len(routes)}")
```

Output:

```
Number of unique route names: 181
```

Now, let's check how many different string objects are created for these routes:

```python
# Count unique string object IDs
routeids = {id(row['route']) for row in rows}
print(f"Number of unique route string objects: {len(routeids)}")
```

Output:

```
Number of unique route string objects: 542305
```

This is surprising! There are only 181 unique route names, but over 500,000 unique string objects. This happens because Python creates a new string object for each row, even if the values are the same.

## String Interning to Save Memory

Python provides a way to "intern" (reuse) strings using the `sys.intern()` function. This can save memory when you have many duplicate strings.

Let's demonstrate how string interning works:

```python
import sys

# Without interning
a = 'hello world'
b = 'hello world'
print(f"a is b (without interning): {a is b}")

# With interning
a = sys.intern(a)
b = sys.intern(b)
print(f"a is b (with interning): {a is b}")
```

Output:

```
a is b (without interning): False
a is b (with interning): True
```

Now, let's use string interning when reading the CTA bus data:

```python
import sys
import reader
import tracemalloc

# Start memory tracking
tracemalloc.start()

# Read data with interning for the route column
rows = reader.read_csv_as_dicts('ctabus.csv', [sys.intern, str, str, int])

# Check unique route objects again
routeids = {id(row['route']) for row in rows}
print(f"Number of unique route string objects (with interning): {len(routeids)}")

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

Output:

```
Number of unique route string objects (with interning): 181
Current memory usage: 189.56 MB
Peak memory usage: 209.32 MB
```

Let's restart the interpreter and try interning both route and date strings:

```python
exit()
```

Start Python again:

```bash
python3
```

```python
import sys
import reader
import tracemalloc

# Start memory tracking
tracemalloc.start()

# Read data with interning for both route and date columns
rows = reader.read_csv_as_dicts('ctabus.csv', [sys.intern, sys.intern, str, int])

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage (interning route and date): {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage (interning route and date): {peak / 1024 / 1024:.2f} MB")
```

Output:

```
Current memory usage (interning route and date): 170.23 MB
Peak memory usage (interning route and date): 190.05 MB
```

The memory usage has decreased further by interning both columns. This demonstrates how understanding Python's memory model can help optimize your programs, especially when dealing with large datasets containing repeated values.

Exit the Python interpreter:

```python
exit()
```
