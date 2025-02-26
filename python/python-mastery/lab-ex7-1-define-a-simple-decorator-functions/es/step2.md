# Un decorador real

Pista: Completa lo siguiente en el archivo `validate.py`

En el Ejercicio 6.6, creaste una clase llamada `ValidatedFunction` que era llamada y que cumplía con las anotaciones de tipo. Reescribe esta clase como una función decoradora llamada `validated`. Debería permitirte escribir código como este:

```python
from validate import Integer, validated

@validated
def add(x: Integer, y:Integer) -> Integer:
    return x + y

@validated
def pow(x: Integer, y:Integer) -> Integer:
    return x ** y
```

Así es como deberían funcionar las funciones decoradas:

```python
>>> add(2, 3)
5
>>> add('2', '3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    x: Expected <class 'int'>
    y: Expected <class 'int'>

>>> pow(2, 3)
8
>>> pow(2, -1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 83, in wrapper
    raise TypeError(f'Bad return: {e}') from None
TypeError: Bad return: Expected <class 'int'>
>>>
```

Tu decorador debería tratar de arreglar las excepciones para que muestren información más útil como se muestra. Además, el decorador `@validated` debería funcionar en clases (no necesitas hacer nada especial).

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @validated
    def sell(self, nshares:PositiveInteger):
        self.shares -= nshares
```

Nota: Esta parte no implica mucho código, pero hay muchos detalles complicados. La solución se verá casi igual que en el Ejercicio 6.6. No temas mirar el código de la solución aunque.
