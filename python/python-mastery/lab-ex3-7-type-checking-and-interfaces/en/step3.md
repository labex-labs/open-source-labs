# Creating Algorithm Template Classes

In this step, you will implement a template method pattern using abstract base classes to reduce code duplication in the CSV parsing functionality.

## Understanding the Template Method Pattern

The template method pattern is a behavioral design pattern that defines the program skeleton of an algorithm in a method, deferring some steps to subclasses. It lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.

In our case, we notice that `read_csv_as_dicts()` and `read_csv_as_instances()` in `reader.py` share most of their code, with only minor differences in how they create records from CSV rows.

## Adding the CSVParser Base Class

Open the `reader.py` file and add the `CSVParser` abstract base class at the top of the file (after the imports):

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

This class provides the template for CSV parsing, with the specific record creation logic abstracted into the `make_record()` method.

## Implementing the Concrete Parser Classes

Now, add the concrete parser classes that implement the specific record creation logic:

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

## Refactoring the Original Functions

Finally, refactor the original `read_csv_as_dicts()` and `read_csv_as_instances()` functions to use these new classes:

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

These refactored functions maintain the same interface as before but now leverage the template method pattern internally.

## Testing Your Implementation

Let's test if your refactored code works correctly. Create a file called `test_reader.py` with the following code:

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

Run the test file:

```bash
python test_reader.py
```

You should see output similar to:

```
First stock: Stock('AA', 100, 32.2)
First stock as dict: {'name': 'AA', 'shares': 100, 'price': 32.2}
First stock from direct parser: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

This confirms that your refactored code works correctly - both the original functions and the direct use of parsers produce the expected results.
