# Understanding the Context

In previous exercises, you may have encountered code that reads CSV files and stores the data in various data structures. The purpose of this code is to take raw text data from a CSV file and convert it into more useful Python objects, such as dictionaries or class instances. This conversion is essential because it allows us to work with the data in a more structured and meaningful way within our Python programs.

The typical pattern for reading CSV files often follows a specific structure. Here is an example of a function that reads a CSV file and converts each row into a dictionary:

```python
import csv

def read_csv_as_dicts(filename, types):
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = { name: func(val)
                       for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records
```

Let's break down how this function works. First, it imports the `csv` module, which provides functionality for working with CSV files in Python. The function takes two parameters: `filename`, which is the name of the CSV file to read, and `types`, which is a list of functions used to convert the data in each column to the appropriate data type.

Inside the function, it initializes an empty list called `records` to store the dictionaries representing each row of the CSV file. It then opens the file using the `with` statement, which ensures that the file is properly closed after the block of code is executed. The `csv.reader` function is used to create an iterator that reads each row of the CSV file. The first row is assumed to be the headers, so it is retrieved using the `next` function.

Next, the function iterates over the remaining rows in the CSV file. For each row, it creates a dictionary using a dictionary comprehension. The keys of the dictionary are the column headers, and the values are the result of applying the corresponding type conversion function from the `types` list to the value in the row. Finally, the dictionary is added to the `records` list, and the function returns the list of dictionaries.

Now, let's look at a similar function that reads data from a CSV file into class instances:

```python
def read_csv_as_instances(filename, cls):
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records
```

This function is similar to the previous one, but instead of creating dictionaries, it creates instances of a class. The function takes two parameters: `filename`, which is the name of the CSV file to read, and `cls`, which is the class whose instances will be created.

Inside the function, it follows a similar structure as the previous function. It initializes an empty list called `records` to store the class instances. It then opens the file, reads the headers, and iterates over the remaining rows. For each row, it calls the `from_row` method of the class `cls` to create an instance of the class using the data from the row. The instance is then added to the `records` list, and the function returns the list of instances.

In this lab, we will refactor these functions to make them more flexible and robust. We will also explore Python's type hinting system, which allows us to specify the expected types of the parameters and return values of our functions. This can make our code more readable and easier to understand, especially for other developers who may be working with our code.

Let's start by creating a `reader.py` file and adding these initial functions to it. Make sure to test these functions to ensure they work properly before moving on to the next steps.
