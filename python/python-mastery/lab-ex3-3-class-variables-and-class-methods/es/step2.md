# Constructores alternativos

Quizás la creación de una instancia de `Stock` a partir de una fila de datos crudos se maneje mejor con un constructor alternativo. Modifica la clase `Stock` de modo que tenga una variable de clase `types` y un método de clase `from_row` como este:

```python
class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)
  ...
```

Aquí está cómo probarlo:

```python
>>> row = ['AA', '100', '32.20']
>>> s = Stock.from_row(row)
>>> s.name
'AA'
>>> s.shares
100
>>> s.price
32.2
>>> s.cost()
3220.0000000000005
>>>
```

Observa detenidamente cómo los valores de cadena en la fila se han convertido en un tipo adecuado.
