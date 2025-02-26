# Enteros Mutables

Los enteros de Python normalmente son inmutables. Sin embargo, suponga que desea crear un objeto de entero mutable. Comience creando una clase como esta:

```python
# mutint.py

class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value
```

Prueba:

```python
>>> a = MutInt(3)
>>> a
<__main__.MutInt object at 0x10e79d408>
>>> a.value
3
>>> a.value = 42
>>> a.value
42
>>> a + 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'MutInt' and 'int'
>>>
```

Todo esto es muy emocionante, excepto que realmente nada funciona con este nuevo objeto `MutInt`. La impresión es horrible, ninguno de los operadores matemáticos funciona y, básicamente, es bastante inútil. Bueno, excepto por el hecho de que su valor es mutable, lo cual es cierto.
