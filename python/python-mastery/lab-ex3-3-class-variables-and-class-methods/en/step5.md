# Generalizing

A useful feature of class-methods is that you can use them to put a highly uniform instance creation interface on a wide variety of classes and write general purpose utility functions that use them.

Earlier, you created a file `reader.py` that had some functions for reading CSV data. Add the following `read_csv_as_instances()` function to the file which accepts a class as input and uses the class `from_row()` method to create a list of instances:

```python
# reader.py
...

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records
```

Get rid of the `read_portfolio()` function--you don't need that anymore. If you want to read a list of `Stock` objects, do this:

```python
>>> # Read a portfolio of Stock instances
>>> from reader import read_csv_as_instances
>>> from stock import Stock
>>> portfolio = read_csv_as_instances('portfolio.csv', Stock)
>>> portfolio
[<__main__.Stock object at 0x100674748>,
<__main__.Stock object at 0x1006746d8>,
<__main__.Stock object at 0x1006747b8>,
<__main__.Stock object at 0x100674828>,
<__main__.Stock object at 0x100674898>,
<__main__.Stock object at 0x100674908>,
<__main__.Stock object at 0x100674978>]
>>>
```

Here is another example of how you might use `read_csv_as_instances()` with a completely different class:

```python
>>> class Row:
         def __init__(self, route, date, daytype, numrides):
             self.route = route
             self.date = date
             self.daytype = daytype
             self.numrides = numrides
         @classmethod
         def from_row(cls, row):
             return cls(row[0], row[1], row[2], int(row[3]))

>>> rides = read_csv_as_instances('ctabus.csv', Row)
>>> len(rides)
577563
>>>
```

**Discussion**

This lab illustrates the two most common uses of class variables and class methods. Class variables are often used to hold a global parameter (e.g., a configuration setting) that is shared across all instances. Sometimes subclasses will inherit from the base class and override the setting to change behavior.

Class methods are most commonly used to implement alternate constructors as shown. A common way to spot such class methods is to look for the word "from" in the name. For example, here is an example on built-in dictionaries:

```python
>>> d = dict.fromkeys(['a','b','c'], 0)     # class method
>>> d
{'a': 0, 'c': 0, 'b': 0}
>>>
```
