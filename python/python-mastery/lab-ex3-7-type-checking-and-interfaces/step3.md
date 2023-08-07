# Algorithm Template Classes

The file `reader.py` contains two functions, `read_csv_as_dicts()` and `read_csv_as_instances()`. Both of those functions are almost identical--there is just one tiny bit of code that's different. Maybe that code could be consolidated into a class definition of some sort. Add the following class to the `reader.py` file:

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

This code provides a shell (or template) of the CSV parsing functionality. To use it, you subclass it, add any additional attributes you might need, and redefine the `make_record()` method. For example:

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

Add the above classes to the `reader.py` file. Here's how you would use one of them:

```python
>>> from reader import DictCSVParser
>>> parser = DictCSVParser([str, int, float])
>>> port = parser.parse('portfolio.csv')
>>>
```

It works, but it's kind of annoying. To fix this, reimplement the `read_csv_as_dicts()` and `read_csv_as_instances()` functions to use these classes. Your refactored code should work exactly the same way that it did before. For example:

```python
>>> import reader
>>> import stock
>>> port = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>>
```
