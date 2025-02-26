# アルゴリズムテンプレートクラス

`reader.py` ファイルには、`read_csv_as_dicts()` と `read_csv_as_instances()` の2つの関数が含まれています。これらの関数はほぼ同じで、違いはわずかなコードのみです。おそらくそのコードをまとめて、ある種のクラス定義にすることができます。`reader.py` ファイルに次のクラスを追加してください。

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

このコードはCSV解析機能のシェル（またはテンプレート）を提供します。それを使用するには、サブクラスを作成し、必要な追加属性を追加して、`make_record()` メソッドを再定義します。たとえば：

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

上記のクラスを `reader.py` ファイルに追加してください。これらのクラスの1つを使用する方法は次のとおりです。

```python
>>> from reader import DictCSVParser
>>> parser = DictCSVParser([str, int, float])
>>> port = parser.parse('portfolio.csv')
>>>
```

これは機能しますが、少し面倒です。これを修正するには、`read_csv_as_dicts()` と `read_csv_as_instances()` 関数を再実装して、これらのクラスを使用するようにします。リファクタリングされたコードは、以前とまったく同じように機能する必要があります。たとえば：

```python
>>> import reader
>>> import stock
>>> port = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>>
```
