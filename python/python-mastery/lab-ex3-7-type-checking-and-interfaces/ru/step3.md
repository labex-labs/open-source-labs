# Шаблонные классы алгоритмов

В файле `reader.py` содержатся две функции: `read_csv_as_dicts()` и `read_csv_as_instances()`. Обе эти функции почти идентичны - есть всего одна маленькая часть кода, которая отличается. Возможно, этот код можно объединить в определение какого-то класса. Добавьте следующий класс в файл `reader.py`:

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

Этот код предоставляет основу (или шаблон) функциональности разбора CSV. Чтобы использовать его, вы создаете подкласс, добавляете любые дополнительные атрибуты, которые могут вам понадобиться, и переопределяете метод `make_record()`. Например:

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

Добавьте вышеперечисленные классы в файл `reader.py`. Вот, как можно использовать один из них:

```python
>>> from reader import DictCSVParser
>>> parser = DictCSVParser([str, int, float])
>>> port = parser.parse('portfolio.csv')
>>>
```

Это работает, но немного раздражает. Чтобы исправить это, перереализуйте функции `read_csv_as_dicts()` и `read_csv_as_instances()`, чтобы использовать эти классы. Ваш重构后的代码 должен работать точно так же, как и раньше. Например:

```python
>>> import reader
>>> import stock
>>> port = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>>
```
