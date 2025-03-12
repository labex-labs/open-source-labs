# Creating a Factory Function

When using inheritance, one common challenge is that users have to remember the names of specific formatter classes. This can be quite a hassle, especially as the number of classes grows. To simplify this process, we can create a factory function. A factory function is a special type of function that creates and returns objects. In our case, it will return the appropriate formatter based on a simple format name.

Let's add the following function to your `tableformat.py` file. This function will take a format name as an argument and return the corresponding formatter object.

```python
def create_formatter(format_name):
    """
    Create a formatter of the specified type.

    Args:
        format_name: Name of the formatter ('text', 'csv', 'html')

    Returns:
        A TableFormatter object

    Raises:
        ValueError: If format_name is not recognized
    """
    if format_name == 'text':
        return TextTableFormatter()
    elif format_name == 'csv':
        return CSVTableFormatter()
    elif format_name == 'html':
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown format {format_name}')
```

The `create_formatter()` function is a factory function. It checks the `format_name` argument you provide. If it's 'text', it creates and returns a `TextTableFormatter` object. If it's 'csv', it returns a `CSVTableFormatter` object, and if it's 'html', it returns an `HTMLTableFormatter` object. If the format name is not recognized, it raises a `ValueError`. This way, users can easily select a formatter just by providing a simple name, without having to know the specific class names.

Now, let's test the factory function. We'll use some existing functions and classes to read data from a CSV file and print it in different formats.

```python
import stock
import reader
from tableformat import create_formatter, print_table

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)

# Test with text formatter
formatter = create_formatter('text')
print("\nText Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)

# Test with CSV formatter
formatter = create_formatter('csv')
print("\nCSV Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)

# Test with HTML formatter
formatter = create_formatter('html')
print("\nHTML Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

In this code, we first import the necessary modules and functions. Then we read data from the `portfolio.csv` file and create a `portfolio` object. After that, we test the `create_formatter()` function with different format names: 'text', 'csv', and 'html'. For each format, we create a formatter object, print the format name, and then use the `print_table()` function to print the `portfolio` data in the specified format.

When you run this code, you should see output in all three formats, separated by the format name:

```
Text Format:
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44

CSV Format:
name,shares,price
AA,100,32.2
IBM,50,91.1
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.1
IBM,100,70.44

HTML Format:
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
```

The factory function makes the code more user-friendly because it hides the details of class instantiation. Users don't need to know how to create formatter objects; they just need to specify the format they want.

This pattern of using a factory function to create objects is a common design pattern in object-oriented programming, known as the Factory Pattern. It provides a layer of abstraction between the client code (the code that uses the formatter) and the actual implementation classes (the formatter classes). This makes the code more modular and easier to use.

**Key Concepts Review:**

1. **Abstract Base Class**: The `TableFormatter` class serves as an interface. An interface defines a set of methods that all classes implementing it must have. In our case, all formatter classes must implement the methods defined in the `TableFormatter` class.

2. **Inheritance**: The concrete formatter classes, like `TextTableFormatter`, `CSVTableFormatter`, and `HTMLTableFormatter`, inherit from the base `TableFormatter` class. This means they get the basic structure and methods from the base class and can provide their own specific implementations.

3. **Polymorphism**: The `print_table()` function can work with any formatter that implements the required interface. This means you can pass different formatter objects to the `print_table()` function, and it will work correctly with each one.

4. **Factory Pattern**: The `create_formatter()` function simplifies the creation of formatter objects. It takes care of the details of creating the right object based on the format name, so users don't have to worry about it.

By using these object-oriented principles, we've created a flexible and extensible system for formatting tabular data in various output formats.
