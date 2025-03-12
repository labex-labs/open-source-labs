# Exploring Python's Memory Model

Python's memory model plays a crucial role in determining how objects are stored in memory and how they are referenced. Understanding this model is essential, especially when dealing with large datasets, as it can significantly impact the performance and memory usage of your Python programs. In this step, we'll specifically focus on how string objects are handled in Python and explore ways to optimize memory usage for large datasets.

## String Repetition in Datasets

The CTA bus data contains many repeated values, such as route names. Repeated values in a dataset can lead to inefficient memory usage if not handled properly. To understand the extent of this issue, let's first examine how many unique route strings are in the dataset.

First, open a Python interpreter. You can do this by running the following command in your terminal:

```bash
python3
```

Once the Python interpreter is open, we'll load the CTA bus data and find the unique routes. Here's the code to achieve this:

```python
import reader
rows = reader.read_csv_as_dicts('ctabus.csv', [str, str, str, int])

# Find unique route names
routes = {row['route'] for row in rows}
print(f"Number of unique route names: {len(routes)}")
```

In this code, we first import the `reader` module, which presumably contains a function to read CSV files as dictionaries. We then use the `read_csv_as_dicts` function to load the data from the `ctabus.csv` file. The second argument `[str, str, str, int]` specifies the data types for each column in the CSV file. After that, we use a set comprehension to find all the unique route names in the dataset and print the number of unique route names.

The output should be:

```
Number of unique route names: 181
```

Now, let's check how many different string objects are created for these routes. Even though there are only 181 unique route names, Python might create a new string object for each occurrence of a route name in the dataset. To verify this, we'll use the `id()` function to get the unique identifier of each string object.

```python
# Count unique string object IDs
routeids = {id(row['route']) for row in rows}
print(f"Number of unique route string objects: {len(routeids)}")
```

The output might surprise you:

```
Number of unique route string objects: 542305
```

This shows that there are only 181 unique route names, but over 500,000 unique string objects. This happens because Python creates a new string object for each row, even if the values are the same. This can lead to significant memory waste, especially when dealing with large datasets.

## String Interning to Save Memory

Python provides a way to "intern" (reuse) strings using the `sys.intern()` function. String interning can save memory when you have many duplicate strings in your dataset. When you intern a string, Python checks if an identical string already exists in the intern pool. If it does, it returns a reference to the existing string object instead of creating a new one.

Let's demonstrate how string interning works with a simple example:

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

In this code, we first create two string variables `a` and `b` with the same value without interning. The `is` operator checks if two variables refer to the same object. Without interning, `a` and `b` are different objects, so `a is b` returns `False`. Then, we intern both strings using `sys.intern()`. After interning, `a` and `b` refer to the same object in the intern pool, so `a is b` returns `True`.

The output should be:

```
a is b (without interning): False
a is b (with interning): True
```

Now, let's use string interning when reading the CTA bus data to reduce memory usage. We'll also use the `tracemalloc` module to track the memory usage before and after interning.

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

In this code, we first start memory tracking using `tracemalloc.start()`. Then, we read the CTA bus data with interning for the route column by passing `sys.intern` as the data type for the first column. After that, we check the number of unique route string objects again and print the current and peak memory usage.

The output should be something like:

```
Number of unique route string objects (with interning): 181
Current memory usage: 189.56 MB
Peak memory usage: 209.32 MB
```

Let's restart the interpreter and try interning both route and date strings to see if we can reduce the memory usage further.

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

The output should show a further decrease in memory usage:

```
Current memory usage (interning route and date): 170.23 MB
Peak memory usage (interning route and date): 190.05 MB
```

This demonstrates how understanding Python's memory model and using techniques like string interning can help optimize your programs, especially when dealing with large datasets containing repeated values.

Finally, exit the Python interpreter:

```python
exit()
```
