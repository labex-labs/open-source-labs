# Creating a Factory Function

One challenge with using inheritance is that users need to know the names of specific formatter classes, which can be cumbersome. We can simplify this by creating a factory function that returns the appropriate formatter based on a simple format name.

Add the following function to your `tableformat.py` file:

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

The `create_formatter()` function is a factory function that creates and returns an appropriate formatter based on a simple name like 'text', 'csv', or 'html'. This makes it easier for users to select a formatter without needing to know the specific class names.

Let's test the factory function:

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

You should see output in all three formats, separated by the format name:

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

The factory function makes the code more user-friendly by hiding the details of class instantiation. Users can simply specify the format they want without needing to know about the specific formatter classes.

This pattern - using a factory function to create objects - is a common design pattern in object-oriented programming, known as the Factory Pattern. It provides a layer of abstraction between the client code and the actual implementation classes, making the code more modular and easier to use.

**Key Concepts Review:**

1. **Abstract Base Class**: The `TableFormatter` class serves as an interface that defines the methods that all formatters must implement.

2. **Inheritance**: The concrete formatter classes inherit from the base class and provide specific implementations.

3. **Polymorphism**: The `print_table()` function works with any formatter that implements the required interface.

4. **Factory Pattern**: The `create_formatter()` function simplifies the creation of formatter objects.

By using these object-oriented principles, we've created a flexible and extensible system for formatting tabular data in various output formats.
