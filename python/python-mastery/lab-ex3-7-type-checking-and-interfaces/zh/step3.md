# 算法模板类

文件`reader.py`包含两个函数，`read_csv_as_dicts()`和`read_csv_as_instances()`。这两个函数几乎完全相同——只是有一小段代码不同。也许可以将这段代码合并到某种类定义中。在`reader.py`文件中添加以下类：

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

这段代码提供了CSV解析功能的一个框架（或模板）。要使用它，你可以对其进行子类化，添加任何可能需要的额外属性，并重新定义`make_record()`方法。例如：

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

将上述类添加到`reader.py`文件中。以下是使用其中一个类的方法：

```python
>>> from reader import DictCSVParser
>>> parser = DictCSVParser([str, int, float])
>>> port = parser.parse('portfolio.csv')
>>>
```

它能正常工作，但有点麻烦。为了解决这个问题，重新实现`read_csv_as_dicts()`和`read_csv_as_instances()`函数，以使用这些类。你重构后的代码应该和之前的工作方式完全一样。例如：

```python
>>> import reader
>>> import stock
>>> port = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>>
```
