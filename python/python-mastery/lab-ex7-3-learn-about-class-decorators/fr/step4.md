# Conversion de ligne

Une fonctionnalité manquante de la classe `Structure` est une méthode `from_row()` qui lui permet de fonctionner avec le code de lecture CSV antérieur. Corrigeons cela. Donnez à la classe `Structure` une variable de classe `_types` et la méthode de classe suivante :

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

Modifiez le décorateur `@validate_attributes` de sorte qu'il examine les différents validateurs pour un attribut `expected_type` et l'utilise pour remplir la variable `_types` ci-dessus.

Une fois que vous avez fait cela, vous devriez être en mesure de faire des choses comme ceci :

```python
>>> s = Stock.from_row(['GOOG', '100', '490.1'])
>>> s
Stock('GOOG', 100, 490.1)
>>> import reader
>>> port = reader.read_csv_as_instances('portfolio.csv', Stock)
>>>
```
