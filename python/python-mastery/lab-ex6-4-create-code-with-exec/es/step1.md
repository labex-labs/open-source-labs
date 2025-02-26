# Experimentar con exec()

Defina un fragmento de código de Python en una cadena y pruebe a ejecutarlo:

```python
>>> code = '''
for i in range(n):
    print(i, end=' ')
'''
>>> n = 10
>>> exec(code)
0 1 2 3 4 5 6 7 8 9
>>>
```

Eso es interesante, pero ejecutar fragmentos de código aleatorios no es especialmente útil. Un uso más interesante de `exec()` es en la creación de código como funciones, métodos o clases. Pruebe este ejemplo en el que creamos una función `__init__()` para una clase.

```python
>>> class Stock:
        _fields = ('name','shares', 'price')

>>> argstr = ','.join(Stock._fields)
>>> code = f'def __init__(self, {argstr}):\n'
>>> for name in Stock._fields:
        code += f'    self.{name} = {name}\n'
>>> print(code)
def __init__(self, name,shares,price):
    self.name = name
    self.shares = shares
    self.price = price

>>> locs = { }
>>> exec(code, locs)
>>> Stock.__init__ = locs['__init__']

>>> # Ahora pruebe la clase
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>>
```

En este ejemplo, una función `__init__()` se crea directamente a partir de la variable `_fields`. No hay trucos extraños que involucren un método especial `_init()` o marcos de pila.
