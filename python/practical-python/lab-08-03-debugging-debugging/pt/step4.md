# Depuração com Print

A depuração com `print()` é bastante comum.

_Dica: Certifique-se de usar `repr()`_

```python
def spam(x):
    print('DEBUG:', repr(x))
    ...
```

`repr()` mostra uma representação precisa de um valor. Não a saída de impressão _bonita_.

```python
>>> from decimal import Decimal
>>> x = Decimal('3.4')
# NO `repr`
>>> print(x)
3.4
# WITH `repr`
>>> print(repr(x))
Decimal('3.4')
>>>
```
