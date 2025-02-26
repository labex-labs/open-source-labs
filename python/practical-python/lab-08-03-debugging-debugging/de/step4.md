# Debugging mit print

Das Debugging mit `print()` ist ziemlich üblich.

_Tipp: Stellen Sie sicher, dass Sie `repr()` verwenden._

```python
def spam(x):
    print('DEBUG:', repr(x))
   ...
```

`repr()` zeigt Ihnen eine genaue Darstellung eines Werts. Nicht die _schöne_ Ausgabedruckform.

```python
>>> from decimal import Decimal
>>> x = Decimal('3.4')
# OHNE `repr`
>>> print(x)
3.4
# MIT `repr`
>>> print(repr(x))
Decimal('3.4')
>>>
```
