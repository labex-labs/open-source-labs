# Operadores matemáticos

Puedes hacer que un objeto funcione con varios operadores matemáticos si implementas los métodos adecuados para él. Sin embargo, es tu responsabilidad reconocer otros tipos de datos e implementar el código de conversión adecuado. Modifica la clase `MutInt` dándole un método `__add__()` de la siguiente manera:

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

  ...

    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented
```

Con este cambio, deberías encontrar que puedes sumar tanto enteros como enteros mutables. El resultado es una instancia de `MutInt`. Sumar otros tipos de números da un error:

```python
>>> a = MutInt(3)
>>> b = a + 10
>>> b
MutInt(13)
>>> b.value = 23
>>> c = a + b
>>> c
MutInt(26)
>>> a + 3.5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'MutInt' and 'float'
>>>
```

Un problema con el código es que no funciona cuando se invierte el orden de los operandos. Considera:

```python
>>> a + 10
MutInt(13)
>>> 10 + a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'MutInt'
>>>
```

Esto sucede porque el tipo `int` no conoce `MutInt` y se confunde. Esto se puede corregir agregando un método `__radd__()`. Este método se llama si la primera intento de llamar a `__add__()` no funcionó con el objeto proporcionado.

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

  ...

    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    __radd__ = __add__    # Operandos invertidos
```

Con este cambio, encontrarás que la suma funciona:

```python
>>> a = MutInt(3)
>>> a + 10
MutInt(13)
>>> 10 + a
MutInt(13)
>>>
```

Dado que nuestro entero es mutable, también puedes hacer que reconozca el operador de adición y actualización en el lugar `+=` implementando el método `__iadd__()`:

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

  ...

    def __iadd__(self, other):
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented
```

Esto permite usos interesantes como este:

```python
>>> a = MutInt(3)
>>> b = a
>>> a += 10
>>> a
MutInt(13)
>>> b                 # Observa que b también cambia
MutInt(13)
>>>
```

Puede parecer un poco extraño que `b` también cambie, pero hay características sutiles como esta con los objetos integrados de Python. Por ejemplo:

```python
>>> a = [1,2,3]
>>> b = a
>>> a += [4,5]
>>> a
[1, 2, 3, 4, 5]
>>> b
[1, 2, 3, 4, 5]

>>> c = (1,2,3)
>>> d = c
>>> c += (4,5)
>>> c
(1, 2, 3, 4, 5)
>>> d                  # Explica la diferencia con las listas
(1, 2, 3)
>>>
```
