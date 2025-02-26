# Zeilenkonvertierung

Eine fehlende Funktion in der `Structure`-Klasse ist eine `from_row()`-Methode, die es ihr ermöglicht, mit früherem Code zur CSV-Leseverarbeitung zu arbeiten. Lassen Sie uns das beheben. Geben Sie der `Structure`-Klasse eine `_types`-Klassenvariable und die folgende Klassenmethode:

```python
# structure.py

class Structure:
    _types = ()
 ...
    @classmethod
    def from_row(cls, row):
        rowdata = [ func(val) for func, val in zip(cls._types, row) ]
        return cls(*rowdata)
 ...
```

Ändern Sie den `@validate_attributes`-Dekorator so, dass er die verschiedenen Validatoren auf ein `expected_type`-Attribut überprüft und es verwendet, um die oben genannte `_types`-Variable auszufüllen.

Nachdem Sie dies getan haben, sollten Sie Folgendes tun können:

```python
>>> s = Stock.from_row(['GOOG', '100', '490.1'])
>>> s
Stock('GOOG', 100, 490.1)
>>> import reader
>>> port = reader.read_csv_as_instances('portfolio.csv', Stock)
>>>
```
