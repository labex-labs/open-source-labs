# Measuring Memory Usage with Different Storage Methods

In this step, we'll examine how different ways of storing the data affect memory usage. To do this, we'll use Python's `tracemalloc` module, which helps track memory allocations made by Python.

## Method 1: Storing the Entire File as a Single String

Let's first create a new Python file called `memory_test1.py` in the `/home/labex/project` directory. Open the file in the editor and add the following code:

```python
# memory_test1.py
import tracemalloc

def test_single_string():
    # Start tracking memory
    tracemalloc.start()

    # Read the entire file as a single string
    with open('/home/labex/project/ctabus.csv') as f:
        data = f.read()

    # Get memory usage statistics
    current, peak = tracemalloc.get_traced_memory()

    print(f"File length: {len(data)} characters")
    print(f"Current memory usage: {current/1024/1024:.2f} MB")
    print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

    # Stop tracking memory
    tracemalloc.stop()

if __name__ == "__main__":
    test_single_string()
```

Run this script by executing:

```bash
python3 /home/labex/project/memory_test1.py
```

You should see output similar to:

```
File length: 12361039 characters
Current memory usage: 11.80 MB
Peak memory usage: 23.58 MB
```

The exact numbers may vary, but you should see that the current memory usage is around 12 MB with a peak of about 24 MB.

## Method 2: Storing as a List of Strings

Now, let's create another file `memory_test2.py` to test storing the data as a list of strings:

```python
# memory_test2.py
import tracemalloc

def test_list_of_strings():
    # Start tracking memory
    tracemalloc.start()

    # Read the file as a list of strings (one string per line)
    with open('/home/labex/project/ctabus.csv') as f:
        lines = f.readlines()

    # Get memory usage statistics
    current, peak = tracemalloc.get_traced_memory()

    print(f"Number of lines: {len(lines)}")
    print(f"Current memory usage: {current/1024/1024:.2f} MB")
    print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

    # Stop tracking memory
    tracemalloc.stop()

if __name__ == "__main__":
    test_list_of_strings()
```

Run this script:

```bash
python3 /home/labex/project/memory_test2.py
```

You should see output similar to:

```
Number of lines: 577564
Current memory usage: 43.70 MB
Peak memory usage: 43.74 MB
```

Notice how the memory usage has increased significantly compared to the single string approach. This is because each line in the list is a separate string object with its own memory overhead.

## Understanding the Memory Difference

The memory overhead difference between the two approaches illustrates an important concept in Python programming: object overhead. When you store data as a list of strings, each string is a separate Python object with its own memory overhead. This overhead includes:

1. The Python object header (typically 16-24 bytes per object)
2. The string representation itself
3. Memory alignment padding

In contrast, when you store everything as a single string, you only have one object with one overhead, which is more memory-efficient when considering the total size.

This trade-off between memory efficiency and data accessibility is something to consider when designing programs that work with large datasets.
