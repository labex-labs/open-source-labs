# Creating Algorithm Template Classes

In this step, we're going to use abstract base classes to implement a template method pattern. The goal is to reduce code duplication in the CSV parsing functionality. Code duplication can make your code harder to maintain and update. By using the template method pattern, we can create a common structure for our CSV parsing code and let sub - classes handle the specific details.

## Understanding the Template Method Pattern

The template method pattern is a behavioral design pattern. It's like a blueprint for an algorithm. In a method, it defines the overall structure or the "skeleton" of an algorithm. However, it doesn't fully implement all the steps. Instead, it defers some of the steps to sub - classes. This means that sub - classes can redefine certain parts of the algorithm without changing its overall structure.

In our case, if you look at the `reader.py` file, you'll notice that the `read_csv_as_dicts()` and `read_csv_as_instances()` functions have a lot of similar code. The main difference between them is how they create records from the rows in the CSV file. By using the template method pattern, we can avoid writing the same code multiple times.

## Adding the CSVParser Base Class

Let's start by adding an abstract base class for our CSV parsing. Open the `reader.py` file. We'll add the `CSVParser` abstract base class right at the top of the file, right after the import statements.

```python
# reader.py
import csv
from abc import ABC, abstractmethod

class CSVParser(ABC):
    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass
```

This `CSVParser` class serves as a template for CSV parsing. The `parse` method contains the common steps for reading a CSV file, like opening the file, getting the headers, and iterating over the rows. The specific logic for creating a record from a row is abstracted into the `make_record()` method. Since it's an abstract method, any class that inherits from `CSVParser` must implement this method.

## Implementing the Concrete Parser Classes

Now that we have our base class, we need to create the concrete parser classes. These classes will implement the specific record - creation logic.

```python
class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return { name: func(val) for name, func, val in zip(headers, self.types, row) }

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)
```

The `DictCSVParser` class is used to create records as dictionaries. It takes a list of types in its constructor. The `make_record` method uses these types to convert the values in the row and create a dictionary.

The `InstanceCSVParser` class is used to create records as instances of a class. It takes a class in its constructor. The `make_record` method calls the `from_row` method of that class to create an instance from the row.

## Refactoring the Original Functions

Now, let's refactor the original `read_csv_as_dicts()` and `read_csv_as_instances()` functions to use these new classes.

```python
def read_csv_as_dicts(filename, types):
    '''
    Read a CSV file into a list of dictionaries with appropriate type conversion.
    '''
    parser = DictCSVParser(types)
    return parser.parse(filename)

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances of a class.
    '''
    parser = InstanceCSVParser(cls)
    return parser.parse(filename)
```

These refactored functions have the same interface as the original ones. But internally, they use the new parser classes we just created. This way, we've separated the common CSV parsing logic from the specific record - creation logic.

## Testing Your Implementation

Let's check if our refactored code works correctly. Create a file named `test_reader.py` and add the following code to it.

```python
import reader
import stock

# Test the refactored read_csv_as_instances function
portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("First stock:", portfolio[0])

# Test the refactored read_csv_as_dicts function
portfolio_dicts = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First stock as dict:", portfolio_dicts[0])

# Test direct use of a parser
parser = reader.DictCSVParser([str, int, float])
portfolio_dicts2 = parser.parse('portfolio.csv')
print("First stock from direct parser:", portfolio_dicts2[0])
```

To run the test, open your terminal and execute the following command:

```bash
python test_reader.py
```

You should see output similar to this:

```
First stock: Stock('AA', 100, 32.2)
First stock as dict: {'name': 'AA', 'shares': 100, 'price': 32.2}
First stock from direct parser: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

If you see this output, it means your refactored code is working correctly. Both the original functions and the direct use of parsers are producing the expected results.
