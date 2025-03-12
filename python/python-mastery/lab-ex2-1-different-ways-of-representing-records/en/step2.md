# Measuring Memory Usage with Different Storage Methods

In this step, we're going to look at how different ways of storing data can impact memory usage. Memory usage is an important aspect of programming, especially when dealing with large datasets. To measure the memory used by our Python code, we'll use Python's `tracemalloc` module. This module is very useful as it allows us to track the memory allocations made by Python. By using it, we can see how much memory our data storage methods are consuming.

## Method 1: Storing the Entire File as a Single String

Let's start by creating a new Python file. Navigate to the `/home/labex/project` directory and create a file named `memory_test1.py`. You can use a text editor to open this file. Once the file is open, add the following code to it. This code will read the entire content of a file as a single string and measure the memory usage.

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

After adding the code, save the file. Now, to run this script, open your terminal and execute the following command:

```bash
python3 /home/labex/project/memory_test1.py
```

When you run the script, you should see output similar to this:

```
File length: 12361039 characters
Current memory usage: 11.80 MB
Peak memory usage: 23.58 MB
```

The exact numbers might be different on your system, but generally, you'll notice that the current memory usage is around 12 MB and the peak memory usage is about 24 MB.

## Method 2: Storing as a List of Strings

Next, we'll test another way of storing the data. Create a new file named `memory_test2.py` in the same `/home/labex/project` directory. Open this file in the editor and add the following code. This code reads the file and stores each line as a separate string in a list, and then measures the memory usage.

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

Save the file and then run the script using the following command in the terminal:

```bash
python3 /home/labex/project/memory_test2.py
```

You should see output similar to this:

```
Number of lines: 577564
Current memory usage: 43.70 MB
Peak memory usage: 43.74 MB
```

Notice that the memory usage has increased significantly compared to the previous method of storing the data as a single string. This is because each line in the list is a separate Python string object, and each object has its own memory overhead.

## Understanding the Memory Difference

The difference in memory usage between the two approaches shows an important concept in Python programming called object overhead. When you store data as a list of strings, each string is a separate Python object. Each object has some additional memory requirements, which include:

1. The Python object header (usually 16 - 24 bytes per object). This header contains information about the object, like its type and reference count.
2. The actual string representation itself, which stores the characters of the string.
3. Memory alignment padding. This is extra space added to ensure that the object's memory address is properly aligned for efficient access.

On the other hand, when you store the entire file content as a single string, there is only one object, and thus only one set of overhead. This makes it more memory - efficient when considering the total size of the data.

When designing programs that work with large datasets, you need to consider this trade - off between memory efficiency and data accessibility. Sometimes, it might be more convenient to access data when it's stored in a list of strings, but it will use more memory. Other times, you might prioritize memory efficiency and choose to store the data as a single string.
