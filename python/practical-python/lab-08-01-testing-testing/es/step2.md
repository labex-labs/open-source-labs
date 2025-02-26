# Programación por Contrato

También conocida como Diseño por Contrato, el uso abundante de aserciones es un enfoque para el diseño de software. Establece que los diseñadores de software deben definir especificaciones de interfaz precisas para los componentes del software.

Por ejemplo, es posible que coloques aserciones en todas las entradas de una función.

```python
def add(x, y):
    assert isinstance(x, int), 'Expected int'
    assert isinstance(y, int), 'Expected int'
    return x + y
```

Comprobar las entradas capturará inmediatamente a los llamantes que no están usando argumentos adecuados.

```python
>>> add(2, 3)
5
>>> add('2', '3')
Traceback (most recent call last):
...
AssertionError: Expected int
>>>
```
