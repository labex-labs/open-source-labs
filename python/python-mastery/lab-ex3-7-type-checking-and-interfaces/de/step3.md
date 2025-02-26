# Algorithmusvorlagenklassen

Die Datei `reader.py` enthält zwei Funktionen, `read_csv_as_dicts()` und `read_csv_as_instances()`. Beide Funktionen sind fast identisch - es gibt nur einen winzigen Codeausschnitt, der unterschiedlich ist. Vielleicht könnte dieser Code in eine Klasse definiert werden. Fügen Sie die folgende Klasse zur Datei `reader.py` hinzu:

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

Dieser Code liefert eine Vorlage (oder ein Template) für die CSV-Analysefunktionalität. Um ihn zu verwenden, erben Sie von ihm, fügen Sie beliebige zusätzliche Attribute hinzu und definieren Sie die `make_record()`-Methode neu. Beispielsweise:

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

Fügen Sie die obigen Klassen zur Datei `reader.py` hinzu. So würden Sie eine von ihnen verwenden:

```python
>>> from reader import DictCSVParser
>>> parser = DictCSVParser([str, int, float])
>>> port = parser.parse('portfolio.csv')
>>>
```

Es funktioniert, aber es ist ziemlich nervig. Um das zu beheben, implementieren Sie die Funktionen `read_csv_as_dicts()` und `read_csv_as_instances()` neu, um diese Klassen zu verwenden. Ihr umgebauter Code sollte genauso funktionieren wie zuvor. Beispielsweise:

```python
>>> import reader
>>> import stock
>>> port = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>>
```
