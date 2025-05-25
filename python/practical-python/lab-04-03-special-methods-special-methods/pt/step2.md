# Métodos Especiais para Conversões de String

Objetos têm duas representações de string.

```python
>>> from datetime import date
>>> d = date(2012, 12, 21)
>>> print(d)
2012-12-21
>>> d
datetime.date(2012, 12, 21)
>>>
```

A função `str()` é usada para criar uma saída imprimível agradável:

```python
>>> str(d)
'2012-12-21'
>>>
```

A função `repr()` é usada para criar uma representação mais detalhada para programadores.

```python
>>> repr(d)
'datetime.date(2012, 12, 21)'
>>>
```

Essas funções, `str()` e `repr()`, usam um par de métodos especiais na classe para produzir a string a ser exibida.

```python
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Used with `str()`
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'

    # Used with `repr()`
    def __repr__(self):
        return f'Date({self.year},{self.month},{self.day})'
```

_Nota: A convenção para `__repr__()` é retornar uma string que, quando fornecida a `eval()`, recriará o objeto subjacente. Se isso não for possível, algum tipo de representação facilmente legível é usado em vez disso._
