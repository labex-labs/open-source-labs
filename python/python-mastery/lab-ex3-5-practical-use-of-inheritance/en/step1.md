# Understanding the Problem

In this lab, we will explore how to use inheritance in Python to create extensible and adaptable code. Let's start by examining the existing `print_table()` function that we will be improving.

First, open the `tableformat.py` file in the WebIDE editor:

```
/home/labex/project/tableformat.py
```

You'll see the current implementation of the `print_table()` function that can format and print tabular data. The function accepts a list of records (objects) and a list of field names, and prints a formatted table.

Let's test this function to see how it works. Open a terminal in the WebIDE and run the following Python commands:

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
tableformat.print_table(portfolio, ['name', 'shares', 'price'])
```

You should see the following output:

```
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

This looks good, but the function has a limitation - it only supports one output format (plain text). What if we wanted to output our data in CSV, HTML, or other formats?

Instead of modifying the function for each new format, we can use inheritance to create a more flexible solution:

1. We'll define a base `TableFormatter` class with methods for formatting
2. We'll create various subclasses for different output formats
3. We'll modify the `print_table()` function to work with any formatter

This approach allows us to add new output formats without changing the core functionality of the `print_table()` function.
