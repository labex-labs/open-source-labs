# Understanding the Problem

In this lab, we're going to learn about inheritance in Python and how it can help us create code that is both extensible and adaptable. Inheritance is a powerful concept in object - oriented programming where a class can inherit attributes and methods from another class. This allows us to reuse code and build more complex functionality on top of existing code.

Let's start by looking at the existing `print_table()` function. This function is what we'll be improving to make it more flexible in terms of output formats.

First, you need to open the `tableformat.py` file in the WebIDE editor. The path to this file is as follows:

```
/home/labex/project/tableformat.py
```

Once you open the file, you'll see the current implementation of the `print_table()` function. This function is designed to format and print tabular data. It takes two main inputs: a list of records (which are objects) and a list of field names. Based on these inputs, it prints a nicely formatted table.

Now, let's test this function to see how it works. Open a terminal in the WebIDE and run the following Python commands. These commands import the necessary modules, read data from a CSV file, and then use the `print_table()` function to display the data.

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
tableformat.print_table(portfolio, ['name', 'shares', 'price'])
```

After running these commands, you should see the following output:

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

The output looks good, but there's a limitation to this function. Currently, it only supports one output format, which is plain text. In real - world scenarios, you might want to output your data in different formats like CSV, HTML, or others.

Instead of making changes to the `print_table()` function every time we want to support a new output format, we can use inheritance to create a more flexible solution. Here's how we'll do it:

1. We'll define a base `TableFormatter` class. This class will have methods that are used for formatting data. The base class provides a common structure and functionality that all the subclasses can build upon.
2. We'll create various subclasses. Each subclass will be designed for a different output format. For example, one subclass might be for CSV output, another for HTML output, and so on. These subclasses will inherit the methods from the base class and can also add their own specific functionality.
3. We'll modify the `print_table()` function so that it can work with any formatter. This means that we can pass different subclasses of the `TableFormatter` class to the `print_table()` function, and it will be able to use the appropriate formatting methods.

This approach has a big advantage. It allows us to add new output formats without changing the core functionality of the `print_table()` function. So, as your requirements change and you need to support more output formats, you can easily do so by creating new subclasses.
