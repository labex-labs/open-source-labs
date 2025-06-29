# Comparing Different Data Structures

In Python, data structures are used to organize and store related data. They are like containers that hold different types of information in a structured way. In this step, we'll compare different data structures and see how much memory they use.

Let's create a new file called `compare_structures.py` in the `/home/labex/project` directory. This file will contain the code to read data from a CSV file and store it in different data structures.

```python
# compare_structures.py
import csv
import tracemalloc
from collections import namedtuple

# Define a named tuple for rides data
RideRecord = namedtuple('RideRecord', ['route', 'date', 'daytype', 'rides'])

# A named tuple is a lightweight class that allows you to access its fields by name.
# It's like a tuple, but with named attributes.

# Define a class with __slots__ for memory optimization
class SlottedRideRecord:
    __slots__ = ['route', 'date', 'daytype', 'rides']

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# A class with __slots__ is a memory - optimized class.
# It avoids using an instance dictionary, which saves memory.

# Define a regular class for rides data
class RegularRideRecord:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# A regular class is an object - oriented way to represent data.
# It has named attributes and can have methods.

# Function to read data as tuples
def read_as_tuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = (row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as tuples.
# Tuples are immutable sequences, and you access their elements by numeric index.

# Function to read data as dictionaries
def read_as_dicts(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Get headers
        for row in rows:
            record = {
                'route': row[0],
                'date': row[1],
                'daytype': row[2],
                'rides': int(row[3])
            }
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as dictionaries.
# Dictionaries use key - value pairs, so you can access elements by their names.

# Function to read data as named tuples
def read_as_named_tuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = RideRecord(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as named tuples.
# Named tuples combine the efficiency of tuples with the readability of named access.

# Function to read data as regular class instances
def read_as_regular_classes(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = RegularRideRecord(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as instances of a regular class.
# Regular classes allow you to add methods to your data.

# Function to read data as slotted class instances
def read_as_slotted_classes(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = SlottedRideRecord(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as instances of a slotted class.
# Slotted classes are memory - optimized and still provide named access.

# Function to measure memory usage
def measure_memory(func, filename):
    tracemalloc.start()

    records = func(filename)

    current, peak = tracemalloc.get_traced_memory()

    # Demonstrate how to use each data structure
    first_record = records[0]
    if func.__name__ == 'read_as_tuples':
        route, date, daytype, rides = first_record
    elif func.__name__ == 'read_as_dicts':
        route = first_record['route']
        date = first_record['date']
        daytype = first_record['daytype']
        rides = first_record['rides']
    else:  # named tuples and classes
        route = first_record.route
        date = first_record.date
        daytype = first_record.daytype
        rides = first_record.rides

    print(f"Structure type: {func.__name__}")
    print(f"Record count: {len(records)}")
    print(f"Example access: Route={route}, Date={date}, Rides={rides}")
    print(f"Current memory: {current/1024/1024:.2f} MB")
    print(f"Peak memory: {peak/1024/1024:.2f} MB")
    print("-" * 50)

    tracemalloc.stop()

    return current

if __name__ == "__main__":
    filename = '/home/labex/project/ctabus.csv'

    # Run all memory tests
    print("Memory usage comparison for different data structures:\n")

    results = []
    for reader_func in [
        read_as_tuples,
        read_as_dicts,
        read_as_named_tuples,
        read_as_regular_classes,
        read_as_slotted_classes
    ]:
        memory = measure_memory(reader_func, filename)
        results.append((reader_func.__name__, memory))

    # Sort by memory usage (lowest first)
    results.sort(key=lambda x: x[1])

    print("\nRanking by memory efficiency (most efficient first):")
    for i, (name, memory) in enumerate(results, 1):
        print(f"{i}. {name}: {memory/1024/1024:.2f} MB")
```

Run the script to see the comparison results:

```bash
python3 /home/labex/project/compare_structures.py
```

The output will show the memory usage for each data structure, along with a ranking from most to least memory - efficient.

## Understanding the Different Data Structures

1. **Tuples**:
   - Tuples are lightweight and immutable sequences. This means once you create a tuple, you can't change its elements.
   - You access elements in a tuple by their numeric index, like `record[0]`, `record[1]`, etc.
   - They are very memory - efficient because they have a simple structure.
   - However, they can be less readable because you need to remember the index of each element.

2. **Dictionaries**:
   - Dictionaries use key - value pairs, which allows you to access elements by their names.
   - They are more readable, for example, you can use `record['route']`, `record['date']`, etc.
   - They have higher memory usage because of the hash table overhead used to store the key - value pairs.
   - They are flexible because you can add or remove fields easily.

3. **Named Tuples**:
   - Named tuples combine the efficiency of tuples with the ability to access elements by name.
   - You can access elements using dot notation, like `record.route`, `record.date`, etc.
   - They are immutable, just like regular tuples.
   - They are more memory - efficient than dictionaries.

4. **Regular Classes**:
   - Regular classes follow an object - oriented approach and have named attributes.
   - You can access attributes using dot notation, like `record.route`, `record.date`, etc.
   - You can add methods to a regular class to define behavior.
   - They use more memory because each instance has an instance dictionary to store its attributes.

5. **Classes with **slots\*\*\*\*:
   - Classes with `__slots__` are memory - optimized classes. They avoid using an instance dictionary, which saves memory.
   - They still provide named access to attributes, like `record.route`, `record.date`, etc.
   - They restrict adding new attributes after the object is created.
   - They are more memory - efficient than regular classes.

## When to Use Each Approach

- **Tuples**: Use tuples when memory is a critical factor and you only need simple indexed access to your data.
- **Dictionaries**: Use dictionaries when you need flexibility, such as when the fields in your data may vary.
- **Named Tuples**: Use named tuples when you need both readability and memory efficiency.
- **Regular Classes**: Use regular classes when you need to add behavior (methods) to your data.
- **Classes with **slots\*\*\*\*: Use classes with `__slots__` when you need behavior and maximum memory efficiency.

By choosing the right data structure for your needs, you can significantly improve the performance and memory usage of your Python programs, especially when working with large datasets.
