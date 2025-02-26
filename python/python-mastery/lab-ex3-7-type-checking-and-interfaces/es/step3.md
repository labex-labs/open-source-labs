# Clases de Plantilla de Algoritmo

El archivo `reader.py` contiene dos funciones, `read_csv_as_dicts()` y `read_csv_as_instances()`. Ambas funciones son casi idénticas, solo hay un pequeño trozo de código que es diferente. Quizás ese código podría consolidarse en una definición de clase de algún tipo. Agrega la siguiente clase al archivo `reader.py`:

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

Este código proporciona una estructura (o plantilla) de la funcionalidad de análisis de CSV. Para usarlo, se crea una subclase, se agregan cualquier atributo adicional que se pueda necesitar y se redefine el método `make_record()`. Por ejemplo:

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

Agrega las clases anteriores al archivo `reader.py`. Aquí está cómo se usaría una de ellas:

```python
>>> from reader import DictCSVParser
>>> parser = DictCSVParser([str, int, float])
>>> port = parser.parse('portfolio.csv')
>>>
```

Funciona, pero es un poco molesto. Para solucionar esto, reimplementa las funciones `read_csv_as_dicts()` y `read_csv_as_instances()` para usar estas clases. Tu código refactorizado debería funcionar exactamente de la misma manera que lo hizo antes. Por ejemplo:

```python
>>> import reader
>>> import stock
>>> port = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>>
```
